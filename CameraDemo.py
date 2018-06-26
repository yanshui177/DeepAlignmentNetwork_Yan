# coding:utf-8
from FaceAlignment import FaceAlignment
import numpy as np
import cv2
import utils
import globalvariable as gvar
import socket               # 导入 socket 模块


# Change this to True if you want to use the DAN-Menpo-tracking.npz model,
# which is able to detect when face tracking is lost.
useTrackingModel = False
port = 12344

if useTrackingModel:
    model = FaceAlignment(112, 112, 1, 1, True)
    model.loadNetwork("model/DAN-Menpo-tracking.npz")
else:
    model = FaceAlignment(112, 112, 1, 2)
    model.loadNetwork("model/DAN-Menpo.npz")

vidIn = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")

neutral_face_flag = True
neutral_landmarks_std = []
reset = True
landmarks = None

print ("Press space to detect the face, press escape to exit")

while True:
    vis = vidIn.read()[1]
    if len(vis.shape) > 2:
        img = np.mean(vis, axis=2).astype(np.uint8)
    else:
        img = vis.astype(np.uint8)

    if reset:
        rects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50)) 
        if len(rects) > 0:
            minX = rects[0][0]
            maxX = rects[0][0] + rects[0][2]
            minY = rects[0][1]
            maxY = rects[0][1] + rects[0][3]
            cv2.rectangle(vis, (minX, minY), (maxX, maxY), (255, 0, 0))
            initLandmarks = utils.bestFitRect(None, model.initLandmarks, [minX, minY, maxX, maxY])
            reset = False

            if model.confidenceLayer:
                landmarks, confidence = model.processImg(img[np.newaxis], initLandmarks)
                if confidence < 0.1:
                    reset = True
            else:
                landmarks = model.processImg(img[np.newaxis], initLandmarks)
            landmarks = landmarks.astype(np.int32)
            for i in range(landmarks.shape[0]):
                cv2.circle(vis, (landmarks[i, 0], landmarks[i, 1]), 2, (0, 255, 0))

            # 以鼻子为原点，计算其余所有点的坐标
            landmarks = landmarks.astype(np.float)
            landmarks_std = landmarks - landmarks[30]  # 所有坐标以鼻尖点为中心

            if neutral_face_flag:
                neutral_landmarks_std = landmarks_std
                neutral_face_flag = False
            else:
                landmarks_std = landmarks_std - neutral_landmarks_std
                # pos_nosetip = landmarks[30]
                # pos_lefteye = (landmarks[36] + landmarks[39]) / 2
                # pos_righteye = (landmarks[42] + landmarks[45]) / 2
                bottom = max(landmarks_std[:, 1])
                top = min(landmarks_std[:, 1])
                left = min(landmarks_std[:, 0])
                right = max(landmarks_std[:, 0])

                landmarks_std[:, 0] = landmarks_std[:, 0] / (right - left)
                landmarks_std[:, 1] = landmarks_std[:, 1] / (bottom - top)

                g_fAU4 = 0.3 * (landmarks_std[17, 1] + 0.35) + \
                         0.3 * (landmarks_std[18, 1] + 0.4) + \
                         0.3 * (landmarks_std[19, 1] + 0.4) + \
                         0.3 * (landmarks_std[20, 1] + 0.4) + \
                         0.3 * (landmarks_std[21, 1] + 0.38)
                if g_fAU4 < 0:
                    g_fAU4 = 0
                if g_fAU4 > 1:
                    g_fAU4 = 1

                gvar.set_g_fAU4(g_fAU4)
                print(g_fAU4)

                # create the string
                info = "g_fAU4:" + str(g_fAU4)

                # send the flag to client
                s = socket.socket()  # 创建 socket 对象
                host = socket.gethostname()  # 获取本地主机名
                s.connect((host, port))
                s.send(info)
                s.close()
    else:
        initLandmarks = utils.bestFitRect(landmarks, model.initLandmarks)
        if model.confidenceLayer:
            landmarks, confidence = model.processImg(img[np.newaxis], initLandmarks)
            if confidence < 0.1:
                reset = True
        else:
            landmarks = model.processImg(img[np.newaxis], initLandmarks)    
        landmarks = np.round(landmarks).astype(np.int32)
        
        for i in range(landmarks.shape[0]):
            cv2.circle(vis, (landmarks[i, 0], landmarks[i, 1]), 2, (0, 255, 0))

        # # # # # # #
        pos_nosetip = landmarks[30]
        pos_lefteye = (landmarks[36] + landmarks[39]) / 2
        pos_righteye = (landmarks[42] + landmarks[45]) / 2

        # 以鼻子为原点，计算其余所有点的坐标
        landmarks = landmarks.astype(np.float)
        landmarks_std = landmarks - landmarks[30]  # 所有坐标以鼻尖点为中心
        # landmarks_std[:, 1] = -landmarks_std[:, 1]  # 转换为常用的标准四象限坐标
        if neutral_face_flag:
            neutral_landmarks_std = landmarks_std
            neutral_face_flag = False
        else:
            # pos_nosetip = landmarks[30]
            # pos_lefteye = (landmarks[36] + landmarks[39]) / 2
            # pos_righteye = (landmarks[42] + landmarks[45]) / 2
            bottom = max(landmarks_std[:, 1])
            top = min(landmarks_std[:, 1])
            left = min(landmarks_std[:, 0])
            right = max(landmarks_std[:, 0])

            landmarks_std[:, 0] = landmarks_std[:, 0] / (right - left)
            landmarks_std[:, 1] = landmarks_std[:, 1] / (bottom - top)

            # # 检验眉毛
            # landmarks_std[[i for i in range(17, 22)]]  # left
            # landmarks_std[[i for i in range(22, 27)]]  # right
            #
            g_fAU4 = 0.3 * (landmarks_std[17, 1] + 0.35) + \
                     0.3 * (landmarks_std[18, 1] + 0.4) + \
                     0.3 * (landmarks_std[19, 1] + 0.4) + \
                     0.3 * (landmarks_std[20, 1] + 0.4) + \
                     0.3 * (landmarks_std[21, 1] + 0.38)
            if g_fAU4 < 0:
                g_fAU4 = 0
            if g_fAU4 > 1:
                g_fAU4 = 1

            gvar.set_g_fAU4(g_fAU4)
            print(g_fAU4)

            # create the string
            info = "g_fAU4:" + str(g_fAU4)

            # send the flag to client
            s = socket.socket()  # 创建 socket 对象
            host = socket.gethostname()  # 获取本地主机名
            s.connect((host, port))
            s.send(info)
            s.close()

    cv2.imshow("image", vis)
    key = cv2.waitKey(1)

    if key == 27:
        break
    if key == 32:
        reset = True

s.close()
