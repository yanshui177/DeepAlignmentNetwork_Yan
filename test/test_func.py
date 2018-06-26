import pickle
import cv2
import numpy

with open("landmarks1.pkl", "r") as p:
    landmarks1 = pickle.load(p)
    img1 = pickle.load(p)
with open("landmarks2.pkl", "r") as p:
    landmarks2 = pickle.load(p)
    img2 = pickle.load(p)


# Procrustes analysis
def transformation_from_points(points1, points2):
    points1 = points1.astype(numpy.float64)
    points2 = points2.astype(numpy.float64)

    c1 = numpy.mean(points1, axis=0)
    c2 = numpy.mean(points2, axis=0)
    points1 -= c1
    points2 -= c2

    s1 = numpy.std(points1)
    s2 = numpy.std(points2)
    points1 /= s1
    points2 /= s2

    U, S, Vt = numpy.linalg.svd(numpy.dot(points1.T, points2))
    R = (U * Vt).T

    return numpy.vstack([numpy.hstack(((s2 / s1) * R,
                                       c2.T - (s2 / s1) * numpy.dot(R, c1.T))),
                         numpy.matrix([0., 0., 1.])])

if __name__ == "__main__":
    M = transformation_from_points(landmarks1, landmarks2)
