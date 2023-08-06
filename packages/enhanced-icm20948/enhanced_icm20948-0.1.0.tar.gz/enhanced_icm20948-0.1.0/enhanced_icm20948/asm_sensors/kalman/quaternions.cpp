#include "filters/eigen3/Eigen/Core"
#include "filters/eigen3/Eigen/Geometry"
#include <chrono>
#include "orientation.hpp"

typedef QuaternionType RawQuaternion;
typedef ControlType Control;
typedef MeasurementType Measurement;
typedef ExtraParametersType ExtraParameters;

int main(void) {
    auto systemModel = OrientationSystemModel();
    auto measurementModel = OrientationMeasurementModel();
    Kalman::ExtendedKalmanFilter<QuaternionType, ControlType, MeasurementType, ExtraParametersType> OrientationFilter;
    Control u(0, 0, 0.3, 0, 0, -0.3, 0.1);
    Measurement z(0, 0, 1.0, 0, 0, 0.3, 0);
    ExtraParameters p(0, 0, -1.0, 0, 0, -0.3, 0, 0, 1.0, 0, 0, 0.3);
    RawQuaternion x_k(1.0, 0, 0, 0);

    OrientationFilter.init(x_k);
    systemModel.P *= 10.0;
    Eigen::Matrix<double, 4, 4> initP;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            initP(i, j) = 1.0;
        }
    }
    systemModel.P;
    
    RawQuaternion result;
    // auto start = std::chrono::system_clock::now();
    for (int i = 0; i < 2000; i++) {
        result = OrientationFilter.predict(systemModel, u);
        printf("%.2lf, %.2lf, %.2lf, %.2lf\n", result(0), result(1), result(2), result(3));
        result = OrientationFilter.update(measurementModel, z, p);
        printf("%.2lf, %.2lf, %.2lf, %.2lf\n", result(0), result(1), result(2), result(3));
        getchar();
    }
    // auto end = std::chrono::system_clock::now();
    // auto duration_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    // printf("Total Time: %ld -> %.2lf, %.2lf, %.2lf, %.2lf\n",duration_ms.count() , result(0), result(1), result(2), result(3));
    
}