# coding:utf-8
import cPickle as pickle
import cv2
import numpy as np


with open("landmarks.pkl", "r") as p:
    landmarks = pickle.load(p)
    img = pickle.load(p)

for i in range(landmarks.shape[0]):
    print(i)
    cv2.circle(img, (landmarks[i, 0], landmarks[i, 1]), 2, (0, 255, 0))

# cv2.imshow("image", img)
# key = cv2.waitKey(0)
pos_nosetip = landmarks[30]
pos_lefteye = (landmarks[36] + landmarks[39]) / 2
pos_righteye = (landmarks[42] + landmarks[45]) / 2

# 以鼻子为原点，计算其余所有点的坐标
landmarks = landmarks.astype(np.float)
landmarks_std = landmarks -landmarks[30]  # 所有坐标以鼻尖点为中心
# landmarks_std[:, 1] = -landmarks_std[:, 1]  # 转换为常用的标准四象限坐标
bottom = max(landmarks_std[:, 1])
top = min(landmarks_std[:, 1])
left = min(landmarks_std[:, 0])
right = max(landmarks_std[:, 0])

landmarks_std[:, 0] = landmarks_std[:, 0] / (right-left)
landmarks_std[:, 1] = landmarks_std[:, 1] / (bottom-top)

# # 检验眉毛
# landmarks_std[[i for i in range(17, 22)]]  # left
# landmarks_std[[i for i in range(22, 27)]]  # right
#
g_fAU4 = 0.25 * (landmarks_std[17, 1] + 0.35) + \
         0.25 * (landmarks_std[18, 1] + 0.4) + \
         0.25 * (landmarks_std[19, 1] + 0.4) + \
         0.25 * (landmarks_std[20, 1] + 0.4) + \
         0.25 * (landmarks_std[21, 1] + 0.38)
if g_fAU4 < 0:
    g_fAU4 = 0
if g_fAU4 >1:
    g_fAU4 = 1

print(g_fAU4)

# landmarks_std[22]

# # 检验眼睛
# landmarks_std[[i for i in range(36, 40)]]  # left
# landmarks_std[[i for i in range(40, 42)]]  # left
# landmarks_std[[i for i in range(42, 46)]]  # right
# landmarks_std[[i for i in range(46, 48)]]  # right
#
# # 检验鼻子
# landmarks_std[[i for i in range(31, 36)]]  # left
#
# # 检验嘴唇
# landmarks_std[[i for i in range(48, 55)]]  # up lips1
# landmarks_std[[i for i in range(60, 65)]]  # up lips2
# landmarks_std[[i for i in range(64, 68)]]  # down lips1
# landmarks_std[[i for i in range(54, 61)]]  # down lips2

# 检验下吧
# landmarks_std[[i for i in range(5, 11)]]



