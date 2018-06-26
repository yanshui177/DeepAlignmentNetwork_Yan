# coding:utf-8
import cPickle as pickle
import cv2
import numpy as np


FACE_POINTS = list(range(17, 68))
MOUTH_POINTS = list(range(48, 61))
RIGHT_BROW_POINTS = list(range(17, 22))
LEFT_BROW_POINTS = list(range(22, 27))
RIGHT_EYE_POINTS = list(range(36, 42))
LEFT_EYE_POINTS = list(range(42, 48))
NOSE_POINTS = list(range(27, 35))
JAW_POINTS = list(range(0, 17))

# Points used to line up the images.
ALIGN_POINTS = (LEFT_BROW_POINTS + RIGHT_EYE_POINTS + LEFT_EYE_POINTS +
                RIGHT_BROW_POINTS + NOSE_POINTS + MOUTH_POINTS)

with open("landmarks1.pkl", "r") as p:
    landmarks1 = pickle.load(p)
    img1 = pickle.load(p)
with open("landmarks2.pkl", "r") as p:
    landmarks2 = pickle.load(p)
    img2 = pickle.load(p)


points1 = landmarks1
points2 = landmarks2

# def transformation_from_points(points1, points2):
"""
Return an affine transformation [s * R | T] such that:
    sum ||s*R*p1,i + T - p2,i||^2
is minimized.
"""
# Solve the procrustes problem by subtracting centroids, scaling by the
# standard deviation, and then using the SVD to calculate the rotation. See
# the following for more details:
#   https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem
points1 = points1.astype(np.float64)
points2 = points2.astype(np.float64)

c1 = np.mean(points1, axis=0)
c2 = np.mean(points2, axis=0)
points1 -= c1
points2 -= c2  # make it mean as 0

s1 = np.std(points1)  # calculate the  standard minus
s2 = np.std(points2)
points1 /= s1  
points2 /= s2

U, S, Vt = np.linalg.svd(np.matmul(points1.T , points2))

# The R we seek is in fact the transpose of the one given by U * Vt. This
# is because the above formulation assumes the matrix goes on the right
# (with row vectors) where as our solution requires the matrix to be on the
# left (with column vectors).
R = (U * Vt).T

np.vstack([np.hstack(((s2 / s1) * R, 
                      c2.T - (s2 / s1) * np.matmul(R, c1.T))),
           np.matrix([0., 0., 1.])])


M = transformation_from_points(landmarks1[ALIGN_POINTS],
                               landmarks2[ALIGN_POINTS])


# def transformation_from_points(points1, points2):
#     """
#     Return an affine transformation [s * R | T] such that:
#         sum ||s*R*p1,i + T - p2,i||^2
#     is minimized.
#     """
#     # Solve the procrustes problem by subtracting centroids, scaling by the
#     # standard deviation, and then using the SVD to calculate the rotation. See
#     # the following for more details:
#     #   https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem
#
#     points1 = points1.astype(np.float64)
#     points2 = points2.astype(np.float64)
#
#     c1 = np.mean(points1, axis=0)
#     c2 = np.mean(points2, axis=0)
#     points1 -= c1
#     points2 -= c2
#
#     s1 = np.std(points1)
#     s2 = np.std(points2)
#     points1 /= s1
#     points2 /= s2
#
#     U, S, Vt = np.linalg.svd(points1.T * points2)
#
#     # The R we seek is in fact the transpose of the one given by U * Vt. This
#     # is because the above formulation assumes the matrix goes on the right
#     # (with row vectors) where as our solution requires the matrix to be on the
#     # left (with column vectors).
#     R = (U * Vt).T
#
#     return np.vstack([np.hstack(((s2 / s1) * R,
#                                        c2.T - (s2 / s1) * R * c1.T)),
#                          np.matrix([0., 0., 1.])])
