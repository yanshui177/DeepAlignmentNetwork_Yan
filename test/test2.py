# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(100)]

# fig, ax = plt.figure()

plt.axis([1, 3, 1, 3])
plt.ion()

while True:
    y = np.random.random(100)
    plt.clf()
    plt.plot(x, y)
    plt.pause(0.1)
