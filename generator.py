import matplotlib.pyplot as plt
import numpy as np
import csv
from math import sin, cos


# k+u\sin\left(x+a\right)+v\cos\left(x+b\right)+w\sin2\left(x+c\right)+p\cos2\left(x+d\right)+q\sin3\left(x+f\right)+s\cos3\left(x+g\right)


def function(x):
    k = -1.3
    s = 10.6
    p = 1.7
    q = 13.4
    u = -0.4
    v = -5.2
    w = -3.6
    g = -1
    d = -1.6
    f = -1.6
    c = -2.6
    b = -2.3 
    a = -2.6
    return k + (k-a)*x - (k-b)*x**2 + u*sin(x+a) + v*cos(x+b) + w*sin(2*(x+c)) + p*cos(2*(x+d)) + q*sin(3*(x+f)) + s*cos(3*(x+g))


xvals = np.linspace(-7,7,500)
fvals = []
for i in xvals:
    fvals.append(function(i))
fvals = np.array(fvals)
plt.plot(xvals,fvals)
plt.title("iteration {frame}")
plt.show()

with open("data.csv", "w", newline= "") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["X","FX"])
    for i,j in zip(xvals, fvals):
        csv_writer.writerow([i,j])