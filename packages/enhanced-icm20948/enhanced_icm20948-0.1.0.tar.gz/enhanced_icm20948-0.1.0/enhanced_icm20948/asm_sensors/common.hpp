#ifndef _COMMON_HPP_
#define _COMMON_HPP_


#include "mraa/common.hpp"
#include "mraa/i2c.hpp"
#include "kalman/orientation.hpp"
#include <iostream>
#include <unistd.h>
#include <assert.h>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include <string>
#include <vector>
#include <map>
#include <thread>
#include <mutex>
#include <atomic>
#include <pybind11/pybind11.h>

namespace py = pybind11;

uint8_t sensorId = 0;

class SensorBatch;
class Sensor {
    protected:
        uint8_t _sensorId;
        uint8_t _i2cBus;
        uint8_t _i2cAddress;

        std::atomic<bool> _isReading;
        
        friend class SensorBatch;
        friend void sensor_reading_thread(std::atomic<bool>&, std::vector<Sensor*>&, std::atomic<double>&);
        friend void orientation_estimating_thread(std::atomic<bool>& terminate, std::vector<Sensor*> sensorPtrArray, Sensor* lastSensor);
        virtual void _sync_read_data(mraa::I2c& i2cBus) {

        }
        virtual void _async_read_data(mraa::I2c& i2cBus) {

        }
        virtual void _await_read_data(mraa::I2c& i2cBus) {

        }
        virtual void _init(mraa::I2c& i2cBus) {
            
        }
        virtual void _configure(mraa::I2c& i2cBus) {

        }
        virtual void _close(mraa::I2c& i2cBus) {

        }
        virtual bool _data_available(void) {
            return false;
        }
        virtual double* _get_latest_data(void) {
            return nullptr;
        }
        virtual void update_orientation(void* state) {

        }
    public:
        std::string sensorName;
        Sensor(uint8_t i2cBus, uint8_t i2cAddress)
        : _i2cBus(i2cBus), _i2cAddress(i2cAddress)
        {
            sensorName = "Sensor" + std::to_string(sensorId);
            _sensorId = sensorId;
            sensorId++;
        }
        
        virtual uint8_t get_sensor_id(void) const {
            return  _sensorId;
        }
        virtual uint8_t get_i2c_address(void) const {
            return _i2cAddress;
        }
        virtual uint8_t get_i2c_bus(void) const {
            return _i2cBus;
        }
        virtual double get_max_frequency(void) {
            return 0.0;
        }

};

void sensor_reading_thread(std::atomic<bool>& terminate, std::vector<Sensor*>& sensorPtrArray, std::atomic<double>& internalMaxFreq) {
    int sensorArraySize = sensorPtrArray.size();
    double sensorMaxFreq = 0.0;
    internalMaxFreq = 1e6;
    mraa::I2c i2cBus(sensorPtrArray[0]->_i2cBus);
    for (int i = 0; i < sensorArraySize; i++) {
        sensorPtrArray[i]->_init(i2cBus);
        sensorPtrArray[i]->_configure(i2cBus);
    }

    for (int i = 0; i < sensorArraySize; i++) {
        if (sensorMaxFreq < sensorPtrArray[i]->get_max_frequency()) {
            sensorMaxFreq = sensorPtrArray[i]->get_max_frequency();
        }
    }

    while (!terminate.load()) {
        auto start = std::chrono::system_clock::now();
        for (int i = 0; i < sensorArraySize; i++) {
            sensorPtrArray[i]->_async_read_data(i2cBus);
        }

        for (int i = 0; i < sensorArraySize; i++) {
            sensorPtrArray[i]->_sync_read_data(i2cBus);
        }

        for (int i = 0; i < sensorArraySize; i++) {
            sensorPtrArray[i]->_await_read_data(i2cBus);
        }
        auto end = std::chrono::system_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        internalMaxFreq = 1e6 / duration.count();
        // if (internalMaxFreq.load() > sensorMaxFreq) {
        //     double restTime = (1e6 / sensorMaxFreq - 1e6 / internalMaxFreq.load()) / 2.0;
        //     std::this_thread::sleep_for(std::chrono::microseconds((int64_t)(restTime)));
        // }
        std::this_thread::sleep_for(std::chrono::microseconds(200));
    }

    for (int i = 0; i < sensorArraySize; i++) {
        sensorPtrArray[i]->_close(i2cBus);
    }
}

struct orientationData {
    QuaternionType state;
    ControlType control;
    MeasurementType measurement;
    ExtraParametersType extraParameters;
};

void orientation_estimating_thread(std::atomic<bool>& terminate, std::vector<Sensor*> sensorPtrArray, Sensor* lastSensor) {
    int sensorGroupNumber = sensorPtrArray.size();
    auto kalmanFilterArray = new Kalman::ExtendedKalmanFilter<QuaternionType, ControlType, MeasurementType, ExtraParametersType>[sensorGroupNumber];
    auto systemModelArray = new OrientationSystemModel[sensorGroupNumber];
    auto measurementModelArray = new OrientationMeasurementModel[sensorGroupNumber];
    auto orientationDataArray = new orientationData[sensorPtrArray.size()];
    long count = 0;
    Eigen::Vector<double, 4> initQuaternion(1, 0, 0, 0);
    for (int i = 0; i < sensorGroupNumber; i++) {
        kalmanFilterArray[i].init(initQuaternion);
    }
    auto start = std::chrono::system_clock::now();
    while (!terminate.load()) {
        if (lastSensor->_data_available()) {
            double* baseData = nullptr;
            for (int i = 0; i < sensorGroupNumber; i++) {
                if (!sensorPtrArray[i]->_data_available()) {
                    continue;
                } else {
                    if (baseData == nullptr) {
                        baseData = lastSensor->_get_latest_data();
                    }
                    auto data = sensorPtrArray[i]->_get_latest_data();
                    // Control 
                    // gyro_h
                    orientationDataArray[i].control[0] = baseData[3];
                    orientationDataArray[i].control[1] = baseData[4];
                    orientationDataArray[i].control[2] = baseData[5];
                    // gyro_f
                    orientationDataArray[i].control[3] = data[3];
                    orientationDataArray[i].control[4] = data[4];
                    orientationDataArray[i].control[5] = data[5];
                    // time_interval
                    orientationDataArray[i].control[6] = 0.005;

                    // Measurement
                    // acc_h
                    orientationDataArray[i].measurement[0] = baseData[0];
                    orientationDataArray[i].measurement[1] = baseData[1];
                    orientationDataArray[i].measurement[2] = baseData[2];
                    // gyro_h
                    orientationDataArray[i].measurement[3] = baseData[3];
                    orientationDataArray[i].measurement[4] = baseData[4];
                    orientationDataArray[i].measurement[5] = baseData[5];
                    // 0
                    orientationDataArray[i].measurement[6] = 0;

                    // ExtraParameters
                    // acc_f
                    orientationDataArray[i].extraParameters[0] = data[0];
                    orientationDataArray[i].extraParameters[1] = data[1];
                    orientationDataArray[i].extraParameters[2] = data[2];
                    // gyro_f
                    orientationDataArray[i].extraParameters[3] = data[3];
                    orientationDataArray[i].extraParameters[4] = data[4];
                    orientationDataArray[i].extraParameters[5] = data[5];
                    // acc_h
                    orientationDataArray[i].extraParameters[6] = baseData[0];
                    orientationDataArray[i].extraParameters[7] = baseData[1];
                    orientationDataArray[i].extraParameters[8] = baseData[2];
                    // gyro_h
                    orientationDataArray[i].extraParameters[9] = baseData[3];
                    orientationDataArray[i].extraParameters[10] = baseData[4];
                    orientationDataArray[i].extraParameters[11] = baseData[5];

                    kalmanFilterArray[i].predict(systemModelArray[i], orientationDataArray[i].control);
                    orientationDataArray[i].state = kalmanFilterArray[i].update(measurementModelArray[i], orientationDataArray[i].measurement, orientationDataArray[i].extraParameters);
                    sensorPtrArray[i]->update_orientation((void*)(&orientationDataArray[i].state));
                    count++;
                }
            }
        } else {
            std::this_thread::sleep_for(std::chrono::microseconds(500));
        }
    }
    auto end = std::chrono::system_clock::now();
    auto duration_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    printf("Average Calculation Frequency: %.2lfkHz", double(count) / duration_ms.count());
}

class SensorBatch {
    protected:
        std::map<uint8_t, std::vector<Sensor*>> _sensorPtrMap;
        std::thread* _threadPool;
        std::atomic<bool>* _terminateArray;
        std::atomic<double>* _internalMaxFreq;
        bool _isReading;
        Sensor* _lastSensor;
        std::atomic<bool> _orientationTerminateFlag;
        std::thread _orientationThread;
        
    public:
        SensorBatch() 
        : _threadPool(nullptr), _terminateArray(nullptr), _internalMaxFreq(nullptr), _isReading(false), _lastSensor(nullptr), _orientationTerminateFlag(true)
        {}
        template <typename T>
        bool add_sensor(T& sensor) {
            if (_isReading) {
                fprintf(stderr, "%s -> Warning: Invalid Operation: Sensor is Running\n", sensor.sensorName.c_str());
                return false;
            }
            auto busIndexFound = _sensorPtrMap.find(sensor._i2cBus);
            if (busIndexFound == _sensorPtrMap.end()) {
                _sensorPtrMap.insert(std::pair<uint8_t, std::vector<Sensor*>>(sensor._i2cBus, std::vector<Sensor*>()));
            } else {
                int sensorArraySize = busIndexFound->second.size();
                for (int i = 0; i < sensorArraySize; i++) {
                    if (_sensorPtrMap[sensor._i2cBus][i]->_i2cAddress == sensor._i2cAddress) {
                        fprintf(stderr, "Warning: I2C Address Conflict on `i2c-%hhu` Detected! Sensor: `%s` will NOT be added!\n", sensor._i2cBus, sensor.sensorName.c_str());
                        return false;
                    }
                }
            }
            _sensorPtrMap[sensor._i2cBus].push_back(&sensor);
            _lastSensor = &sensor;
            return true;
        }
        bool start_reading() {
            if (_isReading) {
                fprintf(stderr, "Warning: Nothing to Start!\n");
                return false;
            }
            _isReading = true;
            int mapElementSize = _sensorPtrMap.size();
            int busIndex = 0;
            _threadPool = new std::thread[mapElementSize];
            _terminateArray = new std::atomic<bool>[mapElementSize];
            _internalMaxFreq = new std::atomic<double>[mapElementSize];
            for (auto iter = _sensorPtrMap.begin(); iter != _sensorPtrMap.end(); iter++) {
                _terminateArray[busIndex] = false;
                _internalMaxFreq[busIndex] = 0.0;
                _threadPool[busIndex] = std::thread(
                    sensor_reading_thread,
                    std::ref(_terminateArray[busIndex]),
                    std::ref(iter->second),
                    std::ref(_internalMaxFreq[busIndex])
                );
                busIndex++;
            }
            return true;
        }
        bool stop_reading() {
            if (_terminateArray == nullptr || _threadPool == nullptr || _internalMaxFreq == nullptr) {
                fprintf(stderr, "Warning: Nothing to Stop!\n");
                return false;
            }
            int mapElementSize = _sensorPtrMap.size();
            for (int i = 0; i < mapElementSize; i++) {
                _terminateArray[i] = true;
            }
            for (int i = 0; i < mapElementSize; i++) {
                _threadPool[i].join();
            }

            delete [] _terminateArray;
            delete [] _threadPool;
            delete [] _internalMaxFreq;

            _terminateArray = nullptr;
            _threadPool = nullptr;
            _internalMaxFreq = nullptr;

            _isReading = false;

            return true;
        }

        double get_max_frequency(void) {
            double maxFreq = 1e10;
            int mapElementSize = _sensorPtrMap.size();
            for (int i = 0; i < mapElementSize; i++) {
                double freq = _internalMaxFreq[i].load();
                if (freq < maxFreq) {
                    maxFreq = freq;
                }
            }
            return maxFreq;
        }

        bool start_estimating_orientation(void) {
            if (!_isReading) {
                fprintf(stderr, "Warning: Sensor Reading NOT Started, Invalid Operation\n");
                return false;
            }
            if (_orientationTerminateFlag.load() == false) {
                fprintf(stderr, "Warning: Nothing to Start\n");
                return false;
            }

            std::vector<Sensor*> orientationSensorPtrArray;
            for (auto iter = _sensorPtrMap.begin(); iter != _sensorPtrMap.end(); iter++) {
                int arraySize = iter->second.size();
                for (int i = 0; i < arraySize; i++) {
                    if ((iter->second)[i] != _lastSensor) {
                        orientationSensorPtrArray.push_back((iter->second)[i]);
                    }
                }
            }

            _orientationTerminateFlag = false;
            _orientationThread = std::thread(
                orientation_estimating_thread,
                std::ref(_orientationTerminateFlag),
                orientationSensorPtrArray,
                _lastSensor
            );

            return true;
        }

        bool stop_estimating_orientation(void) {
            if (_orientationTerminateFlag.load() == true) {
                fprintf(stderr, "Warning: Nothing to Stop\n");
                return false;
            }
            _orientationTerminateFlag = true;
            _orientationThread.join();
            return true;
        }
};

#endif