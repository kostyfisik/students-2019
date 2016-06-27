%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt

n=1800 #number of points
tau=n//50 #width of the puls
t0=10.0*tau #delay of the source
tot_time=int(n+t0)
source_point=n//2

epsilon = 1
c = 1/np.sqrt(epsilon)
a = (c-1)/(c+1)
b = 2/(c+1)
#left
l0_1n,l0_n,l0_n1 = 0,0,0 #z = 0
l1_1n,l1_n,l1_n1 = 0,0,0 #z = 1
#right
r0_1n,r0_n,r0_n1 = 0,0,0 #z = n
r1_1n,r1_n,r1_n1 = 0,0,0 #z = n-1

def source(t, t0, tau):
    return math.exp(-(t-t0)**2/(2.0 * tau**2))

def drawplot(z, ex, hy, q):
    fig = plt.figure()
    plt.title("After t=%i"%q)
    plt.grid(True)
    plt.xlabel(u'Coordinate z')
    plt.ylabel(u'Function')
    ax = fig.add_subplot(211)
    ax.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    ax.plot(z, hy, '--', color='red', linewidth=2, label=u'Hy')
    bx = fig.add_subplot(212)
    bx.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    plt.savefig("step0-at-time-%i.png"%q, fmt='png')
    plt.draw()

ex=np.zeros(n)
hy=np.zeros(n)
z=np.linspace(0,n-1,n)

for q in range(tot_time):
    hy[:-1] += ex[1:] - ex[:-1]
    #right ABC------------------
    r1_n1 = hy[n-2]
    r0_n1 = a*(r1_n1 + r0_1n) + b*(r0_n + r1_n) - r1_1n
    hy[n-1] = r0_n1
    r0_1n, r1_1n = r0_n, r1_n
    r0_n, r1_n = r0_n1, r1_n1
    #---------------------------
    ex[1:] += (hy[1:] - hy[:-1])/epsilon
    ex[source_point] += source(q,t0,tau)
    #left ABC-------------------
    l1_n1 = ex[1]
    l0_n1 = a*(l1_n1 + l0_1n) + b*(l0_n + l1_n) - l1_1n
    ex[0] = l0_n1
    l0_1n, l1_1n = l0_n, l1_n
    l0_n, l1_n = l0_n1, l1_n1
    #---------------------------
    if q % int(n/20)==0 or q+5>tot_time:
        drawplot(z, ex, hy, q)
