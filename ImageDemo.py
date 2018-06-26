# coding:utf-8
from FaceAlignment import FaceAlignment
import numpy as np
import cv2
import utils
import cPickle as pickle
import globalvariable as gvar

# Change this to True if you want to use the DAN-Menpo-tracking.npz model,
# which is able to detect when face tracking is lost.
useTrackingModel = False

if useTrackingModel:
    model = FaceAlignment(112, 112, 1, 1, True)
    model.loadNetwork("model/DAN-Menpo-tracking.npz")
else:
    model = FaceAlignment(112, 112, 1, 2)
    model.loadNetwork("model/DAN-Menpo.npz")

cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")

reset = True
landmarks = None

print ("Press space to detect the face, press escape to exit")

img = cv2.imread("image/smile.jpg")

if len(img.shape) > 2:
    img = np.mean(img, axis=2).astype(np.uint8)
else:
    img = img.astype(np.uint8)

if reset:
    rects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    if len(rects) > 0:
        minX = rects[0][0]
        maxX = rects[0][0] + rects[0][2]
        minY = rects[0][1]
        maxY = rects[0][1] + rects[0][3]
        cv2.rectangle(img, (minX, minY), (maxX, maxY), (255, 0, 0))
        initLandmarks = utils.bestFitRect(None, model.initLandmarks, [minX, minY, maxX, maxY])
        reset = False

        if model.confidenceLayer:
            landmarks, confidence = model.processImg(img[np.newaxis], initLandmarks)
            if confidence < 0.1:
                reset = True
        else:
            landmarks = model.processImg(img[np.newaxis], initLandmarks)
        landmarks = landmarks.astype(np.int32)

        with open("landmarks.pkl", 'wb') as p:
            pickle.dump(landmarks, p)
            pickle.dump(img, p)

        for i in range(landmarks.shape[0]):
            cv2.circle(img, (landmarks[i, 0], landmarks[i, 1]), 2, (0, 255, 0))
else:
    initLandmarks = utils.bestFitRect(landmarks, model.initLandmarks)
    if model.confidenceLayer:
        landmarks, confidence = model.processImg(img[np.newaxis], initLandmarks)
        if confidence < 0.1:
            reset = True
    else:
        landmarks = model.processImg(img[np.newaxis], initLandmarks)
    landmarks = np.round(landmarks).astype(np.int32)

    with open("landmarks.pkl", 'wb') as p:
        pickle.dump(landmarks, p)
        pickle.dump(img, p)

    for i in range(landmarks.shape[0]):
        cv2.circle(img, (landmarks[i, 0], landmarks[i, 1]), 2, (0, 255, 0))

# output
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

gvar.set_g_fAU4(g_fAU4)

print(g_fAU4)

cv2.imshow("image", img)


key = cv2.waitKey(0)
