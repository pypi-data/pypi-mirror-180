// MIT License

// Copyright (c) 2022 Haoyuan Ma, Chenhao Zhang

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


// The MIT License (MIT)
//
// Copyright (c) 2015 Markus Herb
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
#ifndef KALMAN_EXTENDEDKALMANFILTER_HPP_
#define KALMAN_EXTENDEDKALMANFILTER_HPP_

#include "KalmanFilterBase.hpp"
#include "StandardFilterBase.hpp"
#include "LinearizedSystemModel.hpp"
#include "LinearizedMeasurementModel.hpp"

namespace Kalman {
    
    /**
     * @brief Extended Kalman Filter (EKF)
     * 
     * This implementation is based upon [An Introduction to the Kalman Filter](https://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf)
     * by Greg Welch and Gary Bishop.
     *
     * @param StateType The vector-type of the system state (usually some type derived from Kalman::Vector)
     */
    template<class StateType, class ControlType, class MeasurementType, class ExtraParametersType>
    class ExtendedKalmanFilter : public KalmanFilterBase<StateType>,
                                 public StandardFilterBase<StateType>
    {
    public:
        //! Kalman Filter base type
        typedef KalmanFilterBase<StateType> KalmanBase;
        //! Standard Filter base type
        typedef StandardFilterBase<StateType> StandardBase;
        
        // //! Numeric Scalar Type inherited from base
        // using typename KalmanBase::T;
        
        //! State Type inherited from base
        // using typename KalmanBase::State;
        
        //! Linearized Measurement Model Type
        using MeasurementModelType = LinearizedMeasurementModel<StateType, ControlType, MeasurementType, ExtraParametersType>;
        
        //! Linearized System Model Type
        using SystemModelType = LinearizedSystemModel<StateType, ControlType, MeasurementType, ExtraParametersType>;
        
    public:
        //! Kalman Gain Matrix Type
        using KalmanGain = Kalman::KalmanGain<StateType, MeasurementType>;
        
    public:
        //! State Estimate
        using KalmanBase::x;
        //! State Covariance Matrix
        using StandardBase::P;
        
    public:
        /**
         * @brief Constructor
         */
        ExtendedKalmanFilter()
        {
            // Setup state and covariance
            P.setIdentity();
        }
        
        /**
         * @brief Perform filter prediction step using system model and no control input (i.e. \f$ u = 0 \f$)
         *
         * @param [in] s The System model
         * @return The updated state estimate
         */
        const StateType& predict( SystemModelType& s )
        {
            // predict state (without control)
            ControlType u;
            u.setZero();
            return predict( s, u );
        }
        
        /**
         * @brief Perform filter prediction step using control input \f$u\f$ and corresponding system model
         *
         * @param [in] s The System model
         * @param [in] u The Control input vector
         * @return The updated state estimate
         */
        const StateType& predict( SystemModelType& s, const ControlType& u )
        {
            s.updateJacobians( x, u );
            
            // predict state
            x = s.f(x, u);
            
            // predict covariance
            P  = ( s.F * P * s.F.transpose() ) + ( s.W * s.getCovariance() * s.W.transpose() );
            // printf("F:\n");
            // for (int i = 0; i < 4; i++) {
            //     for (int j = 0; j < 4; j++) {
            //         printf("%.2lf, ", s.F(i, j));
            //     }
            //     printf("\n");
            // }
            // printf("W:\n");
            // for (int i = 0; i < 4; i++) {
            //     for (int j = 0; j < 4; j++) {
            //         printf("%.2lf, ", s.W(i, j));
            //     }
            //     printf("\n");
            // }
            // return state prediction
            return this->getState();
        }
        
        /**
         * @brief Perform filter update step using measurement \f$z\f$ and corresponding measurement model
         *
         * @param [in] m The Measurement model
         * @param [in] z The measurement vector
         * @return The updated state estimate
         */
        const StateType& update( MeasurementModelType& m, const MeasurementType& z, const ExtraParametersType& extraP)
        {
            m.updateExtraParameters( extraP );
            m.updateCovariance( x );
            m.updateJacobians( x );
            
            
            // COMPUTE KALMAN GAIN
            // compute innovation covariance
            Covariance<MeasurementType> S = ( m.H * P * m.H.transpose() ) + ( m.V * m.getCovariance() * m.V.transpose() );
            // printf("S:\n");
            // for (int i = 0; i < 7; i++) {
            //     for (int j = 0; j < 7; j++) {
            //         printf("%.2lf, ", S(i, j));
            //     }
            //     printf("\n");
            // }

            // printf("V:\n");
            // for (int i = 0; i < 7; i++) {
            //     for (int j = 0; j < 7; j++) {
            //         printf("%.2lf, ", m.V(i, j));
            //     }
            //     printf("\n");
            // }

            // printf("P:\n");
            // for (int i = 0; i < 4; i++) {
            //     for (int j = 0; j < 4; j++) {
            //         printf("%.2lf, ", P(i, j));
            //     }
            //     printf("\n");
            // }
            // compute kalman gain
            KalmanGain K = P * m.H.transpose() * S.inverse();
            // printf("K:\n");
            // for (int i = 0; i < 4; i++) {
            //     for (int j = 0; j < 7; j++) {
            //         printf("%.2lf, ", K(i, j));
            //     }
            //     printf("\n");
            // }
            // UPDATE STATE ESTIMATE AND COVARIANCE
            // Update state using computed kalman gain and innovation
            x += K * ( z - m.h( x ) );
            
            // Update covariance
            P -= K * m.H * P;
            // P /= x.norm();
            // x.normalize();
            // printf("P:\n");
            // for (int i = 0; i < 4; i++) {
            //     for (int j = 0; j < 4; j++) {
            //         printf("%.2lf, ", P(i, j));
            //     }
            //     printf("\n");
            // }
            // return updated state estimate
            return this->getState();
        }
    };
}

#endif
