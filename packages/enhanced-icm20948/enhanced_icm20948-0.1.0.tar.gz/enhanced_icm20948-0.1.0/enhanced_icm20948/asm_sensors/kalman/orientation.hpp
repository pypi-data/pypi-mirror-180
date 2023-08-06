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

#ifndef _ORIENTATION_HPP_
#define _ORIENTATION_HPP_

#include "filters/ExtendedKalmanFilter.hpp"
// #include "filters/UnscentedKalmanFilter.hpp"

typedef Eigen::Vector<double, 4> QuaternionType;
typedef Eigen::Vector<double, 7> ControlType;
typedef Eigen::Vector<double, 7> MeasurementType;
typedef Eigen::Vector<double, 12> ExtraParametersType;

class OrientationSystemModel: public Kalman::LinearizedSystemModel<QuaternionType, ControlType, MeasurementType, ExtraParametersType> {

    public:
        virtual void updateJacobians( const State& x, const Control& u )
        {
            double q0q0 = x(0) * x(0);
            double q0q1 = x(0) * x(1);
            double q0q2 = x(0) * x(2);
            double q0q3 = x(0) * x(3);
            double q1q1 = x(1) * x(1);
            double q1q2 = x(1) * x(2);
            double q1q3 = x(1) * x(3);
            double q2q2 = x(2) * x(2);
            double q2q3 = x(2) * x(3);
            double q3q3 = x(3) * x(3);

            Eigen::Vector<double, 3> a11(q0q1, q0q2, q0q3);         Eigen::Vector<double, 3> a12(0.5+q1q1, q1q2, q1q3);
            Eigen::Vector<double, 3> a13(q1q2, 0.5+q2q2, q2q3);     Eigen::Vector<double, 3> a14(q1q3, q2q3, 0.5+q3q3);
            Eigen::Vector<double, 3> a21(-0.5-q0q0, -q0q3, q0q2);   Eigen::Vector<double, 3> a22(-q0q1, -q1q3, q1q2);
            Eigen::Vector<double, 3> a23(-q0q2, -q2q3, 0.5+q2q2);   Eigen::Vector<double, 3> a24(-q0q3, -0.5-q3q3, q2q3);
            Eigen::Vector<double, 3> a31(q0q3, -0.5-q0q0, -q0q1);   Eigen::Vector<double, 3> a32(q1q3, -q0q1, -0.5-q1q1);
            Eigen::Vector<double, 3> a33(q2q3, -q0q2, -q1q2);       Eigen::Vector<double, 3> a34(0.5+q3q3, -q0q3, -q1q3);
            Eigen::Vector<double, 3> a41(-q0q2, q0q1, -0.5-q0q0);   Eigen::Vector<double, 3> a42(-q1q2, 0.5+q1q1, -q0q1);
            Eigen::Vector<double, 3> a43(-0.5-q2q2, q1q2, -q0q2);   Eigen::Vector<double, 3> a44(-q2q3, q1q3, -q0q3);

            
            Eigen::Matrix<double, 4, 4> F2;
            F2.setZero();
            F2(0, 0) = 0;   F2(0, 1) = -u(0);   F2(0, 2) = -u(1);   F2(0, 3) = -u(2);
            F2(1, 0) = u(0);    F2(1, 1) = 0;   F2(1, 2) = u(2);    F2(1, 3) = -u(1);
            F2(2, 0) = u(1);    F2(2, 1) = -u(2);   F2(2, 2) = 0;   F2(2, 3) = u(0);
            F2(3, 0) = u(2);    F2(3, 1) = u(1);    F2(3, 2) = -u(0);   F2(3, 3) = 0;

            // F2(0, 0) = 0;   F2(0, 1) = -u(3);   F2(0, 2) = -u(4);   F2(0, 3) = -u(5);
            // F2(1, 0) = u(3);    F2(1, 1) = 0;   F2(1, 2) = u(5);    F2(1, 3) = -u(4);
            // F2(2, 0) = u(4);    F2(2, 1) = -u(5);   F2(2, 2) = 0;   F2(2, 3) = u(3);
            // F2(3, 0) = u(5);    F2(3, 1) = u(4);    F2(3, 2) = -u(3);   F2(3, 3) = 0;

            Eigen::Matrix<double, 4, 4> F1;
            // Eigen::Quaterniond q_hf_k_1(x(0), x(1), x(2), x(3));
            // Eigen::Quaterniond gyro_f(0, u(3), u(4), u(5));
            // Eigen::Quaterniond e_gyro_h = q_hf_k_1 * gyro_f * q_hf_k_1.inverse();
            // Eigen::Vector<double, 3> W2(e_gyro_h.x(), e_gyro_h.y(), e_gyro_h.z());
            Eigen::Vector<double, 3> W2(u(3), u(4), u(5));
            F1(0, 0) = W2.dot(a11); F1(0, 1) = W2.dot(a12); F1(0, 2) = W2.dot(a13); F1(0, 3) = W2.dot(a14);
            F1(1, 0) = W2.dot(a21); F1(1, 1) = W2.dot(a22); F1(1, 2) = W2.dot(a23); F1(1, 3) = W2.dot(a24);
            F1(2, 0) = W2.dot(a31); F1(2, 1) = W2.dot(a32); F1(2, 2) = W2.dot(a33); F1(2, 3) = W2.dot(a34);
            F1(3, 0) = W2.dot(a41); F1(3, 1) = W2.dot(a42); F1(3, 2) = W2.dot(a43); F1(3, 3) = W2.dot(a44);

            F = (F1 + 0.5*F2) * u(6);
            F(0, 0) += 1;   F(1, 1) += 1;   F(2, 2) += 1;   F(3, 3) += 1;
        }

        virtual State f(const State& x, const Control& u) const {
            Eigen::Quaterniond x_k_1(x(0), x(1), x(2), x(3));
            Eigen::Quaterniond w_ff(0, u(3), u(4), u(5));
            Eigen::Quaterniond w_temp;
            Eigen::Quaterniond x_k;
            Eigen::Vector<double, 3> w_hh(u(0), u(1), u(2));
            Eigen::Vector<double, 3> w_k;

            w_temp = x_k_1 * w_ff * x_k_1.inverse();

            w_k(0) = w_hh(0) - w_temp.x();
            w_k(1) = w_hh(1) - w_temp.y();
            w_k(2) = w_hh(2) - w_temp.z();

            w_k *= 0.5 * u(6);
            w_temp = Eigen::Quaterniond(1, w_k(0), w_k(1), w_k(2));
            x_k = x_k_1 * w_temp;

            // x_k.normalize();
            return State(x_k.w(), x_k.x(), x_k.y(), x_k.z());
        }
};

class OrientationMeasurementModel : public Kalman::LinearizedMeasurementModel<QuaternionType, ControlType, MeasurementType, ExtraParametersType> {
    private:
        ExtraParametersType _extraP;
    public:
        virtual void updateExtraParameters(const ExtraParametersType& extraP) {
            _extraP = extraP;
        }
        virtual Measurement h(const State& x) const {
            Eigen::Quaterniond x_k(x(0), x(1), x(2), x(3));
            Eigen::Quaterniond acc_f(0, _extraP(0), _extraP(1), _extraP(2));
            Eigen::Quaterniond gyro_f(0, _extraP(3), _extraP(4), _extraP(5));

            double norm = x_k.norm();
            Eigen::Quaterniond acc_h = x_k * acc_f * x_k.inverse();
            Eigen::Quaterniond gyro_h = x_k * gyro_f * x_k.inverse();
            // printf("m.h(x): %.2lf, %.2lf, %.2lf, %.2lf, %.2lf, %.2lf\n", acc_h.x(), acc_h.y(), acc_h.z(), gyro_h.x(), gyro_h.y(), gyro_h.z());
            return Measurement(acc_h.x(), acc_h.y(), acc_h.z(), gyro_h.x(), gyro_h.y(), gyro_h.z(), norm*norm-1.0);
        }

        virtual void updateJacobians( const State& x ) {
            Eigen::Vector<double, 3> b11(x(0), x(3), -x(2));        Eigen::Vector<double, 3> b12(x(1), x(2), x(3));
            Eigen::Vector<double, 3> b13(-x(2), x(1), -x(0));       Eigen::Vector<double, 3> b14(-x(3), x(0), x(1));
            Eigen::Vector<double, 3> b21(-x(3), x(0), x(1));        Eigen::Vector<double, 3> b22(x(2), -x(1), x(0));
            Eigen::Vector<double, 3> b23(x(1), x(2), x(3));         Eigen::Vector<double, 3> b24(-x(0), -x(3), x(2));
            Eigen::Vector<double, 3> b31(x(2), -x(1), x(0));        Eigen::Vector<double, 3> b32(x(3), -x(0), -x(1));
            Eigen::Vector<double, 3> b33(x(0), x(3), -x(2));        Eigen::Vector<double, 3> b34(x(1), x(2), x(3));

            Eigen::Vector<double, 3> acc_f(_extraP(0), _extraP(1), _extraP(2));
            Eigen::Vector<double, 3> gyro_f(_extraP(3), _extraP(4), _extraP(5));

            H(0, 0) = acc_f.dot(b11);    H(0, 1) = acc_f.dot(b12);    H(0, 2) = acc_f.dot(b13);    H(0, 3) = acc_f.dot(b14);
            H(1, 0) = acc_f.dot(b21);    H(1, 1) = acc_f.dot(b22);    H(1, 2) = acc_f.dot(b23);    H(1, 3) = acc_f.dot(b24);
            H(2, 0) = acc_f.dot(b31);    H(2, 1) = acc_f.dot(b32);    H(2, 2) = acc_f.dot(b33);    H(2, 3) = acc_f.dot(b34);
            H(3, 0) = gyro_f.dot(b11);   H(3, 1) = gyro_f.dot(b12);   H(3, 2) = gyro_f.dot(b13);   H(3, 3) = gyro_f.dot(b14);
            H(4, 0) = gyro_f.dot(b21);   H(4, 1) = gyro_f.dot(b22);   H(4, 2) = gyro_f.dot(b23);   H(4, 3) = gyro_f.dot(b24);
            H(5, 0) = gyro_f.dot(b31);   H(5, 1) = gyro_f.dot(b32);   H(5, 2) = gyro_f.dot(b33);   H(5, 3) = gyro_f.dot(b34);
            H(6, 0) = x(0);  H(6, 1) = x(1);  H(6, 2) = x(2); H(6, 3) = x(3);
            // printf("H:\n");

            // for (int i = 0; i < 7; i++) {
            //     for (int j = 0; j < 4; j++) {
            //         printf("%.2lf, ", H(i, j));
            //     }
            //     printf("\n");
            // }
            H *= 2;
        }

        virtual void updateCovariance(const State& x) {
            Eigen::Quaterniond acc_f(0, _extraP(0), _extraP(1), _extraP(2));
            Eigen::Quaterniond gyro_f(0, _extraP(3), _extraP(4), _extraP(5));
            Eigen::Quaterniond q_hf(x(0), x(1), x(2), x(3));

            Eigen::Quaterniond e_gyro_h = q_hf * gyro_f * q_hf.inverse();
            Eigen::Quaterniond e_acc_h = q_hf * acc_f * q_hf.inverse();
            Eigen::Vector<double, 3> thetaG(_extraP(9)-e_gyro_h.x(), _extraP(10)-e_gyro_h.y(), _extraP(11)-e_gyro_h.z());
            Eigen::Vector<double, 3> thetaA(_extraP(6)-e_acc_h.x(), _extraP(7)-e_acc_h.y(), _extraP(8)-e_acc_h.z());
            double thetaGNorm = thetaG.norm();
            double thetaANorm = thetaA.norm();
            this->P(0, 0) = thetaGNorm;
            this->P(1, 1) = thetaGNorm;
            this->P(2, 2) = thetaGNorm;
            this->P(3, 3) = thetaANorm;
            this->P(4, 4) = thetaANorm;
            this->P(5, 5) = thetaANorm;
            this->P(6, 6) = 0;
            // printf("Measurement Covariance: \n");
            // for (int i = 0; i < 7; i++) {
            //     for (int j = 0; j < 7; j++) {
            //         printf("%.2lf, ", this->P(i, j));
            //     }
            //     printf("\n");
            // }
        }
};


#endif