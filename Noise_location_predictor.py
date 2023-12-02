import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# 1. 단계수(또는 기간)의 정의
n_iters = 50

# 2. 대상의 실제 위치 정의
actual_x = 0
actual_y = 0
Q = np.full((2,2), 0.0001)
print('Q matrix:', Q.shape, '\n\n', Q)

# 3. 소음 위치 측정기 만들기
# 50개의 랜덤 위치를 생성
x_pos = np.random.normal(0, 0.5, n_iters)
y_pos = np.random.normal(0, 0.5, n_iters)

# 위치를 행렬로 표시
measurements = np.stack((x_pos, y_pos), axis=1).reshape((n_iters,2,1))

print('Measurements:', measurements.shape, '\n\n', measurements[0:5], '\n', '...')

# 측정 오차의 공분산
R = np.diag([0.25,0.25])
print('R matrix: ', R.shape, '\n\n', R)

# 4. 빈 배열 만들기
# _hat --> 위치 추정 (칼만 필터의 경우 이 위치를 확률분포로 나타냄)
x_hat = np.zeros((n_iters, 2,1))
P = np.zeros((n_iters, 2,2))
x_hat_min = np.zeros((n_iters, 2,1))
P_min =np.zeros((n_iters, 2,2))
K = np.zeros((n_iters,2,2))

# 초기 상테
x_hat[0] = [[0], [0]]

# 초기 오차 공분산
P[0] = np.diag([1000.0, 1000.0])

print('x_hat[0]:\n\n', x_hat[0], '\n\n P[0] matrix: ', P[0].shape, '\n\n', P[0])

# 5. 수학적 계산을 위한 관련 행렬 정의
A = np.array([[1.0, 0.0],
             [0.0, 1.0]])

# H 행렬
H= np.eye(2)

# Kalman gain을 위한 단위 행렬
I = np.eye(2)

print('A matrix \n\n', A, '\n\n Hmatrix \n\n', H, '\n\n I matrix \n\n', I)

#6. 계산 및 오차 감소 측정
for k in range(1, n_iters):
    # 구할수 있는 추정치 및 오차 공분산 계산
    x_hat_min[k] = A.dot(x_hat[k-1])
    P_min[k] = A.dot(P[k-1]).dot(A.T) + Q

    # Kalman gain 계산
    S = H.dot(P_min[k]).dot(H.T) + R
    K[k] = P_min[k].dot(H.T).dot(inv(S))

    # 사후 추정치 및 오차 공분산 계산
    x_hat[k] = x_hat_min[k] + K[k].dot(measurements[k] - H.dot(x_hat_min[k]))
    P[k] = (I-K[k]).dot(P_min[k])

# 7. 실제 오차 측정 및 추정 위치 시각화
plt.figure(figsize=(7,7))
for n in range(n_iters):
    plt.scatter(float(measurements[n][0]), float(measurements[n][1]),
               color='orange', label='measured position', alpha=0.7)
    plt.scatter(float(x_hat[n][0]), float(x_hat[n][1]),
               color='blue', label='kalman position', alpha=0.3)

    plt.scatter(actual_x, actual_y, color='red', s=100, label='actual position')
    plt.title('Actual Measured and Estimated Positions')
    plt.xlabel('X axis')
    plt.ylabel('y axis')
plt. show()
