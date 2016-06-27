%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt

n = 1800 #number of points
epsilon = 25
tau = (n//50)*np.sqrt(epsilon) #puls width
t0 = 10.0*tau #delay of the source
tot_time = int(n*np.sqrt(epsilon)+t0)
source_point = n//2

pml_width=5 #PML width
eps = epsilon*np.ones(n)

dx = 1
R0 = 10**(-6)
m = 4
  
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
    plt.savefig("step2-at-time-%i.png"%q, fmt='png')
    plt.draw()

ex=np.zeros(n)
hy=np.zeros(n)
z=np.linspace(0,n-1,n)

Smax = -(m+1)*np.log(R0)/2/(pml_width*dx)
Se = np.zeros(n)
Sm = np.zeros(n)

for nn in range(int(pml_width)):
    Se[nn+1] = Smax*((pml_width-nn-0.5)/pml_width)**m
    Sm[nn] = Smax*((pml_width-nn)/pml_width)**m
    Se[n-1-nn] = Smax*((pml_width-nn-0.5)/pml_width)**m  
    Sm[n-1-nn] = Smax*((pml_width-nn)/pml_width)**m
    
Ae = np.exp(-Se) - 1
Be = np.exp(-Se) 
Am = np.exp(-Sm) - 1
Bm = np.exp(-Sm) 

Pm = np.zeros(n)
Pe = np.zeros(n)

for q in range(tot_time):
    Pm[:-1] = Bm[:-1]*Pm[:-1] + Am[:-1]*(ex[1:] - ex[:-1])
    hy[:-1] += ex[1:] - ex[:-1] + Pm[:-1]
    Pe[1:] = Be[1:]*Pe[1:] + Ae[1:]*(hy[1:] - hy[:-1])
    ex[1:] += (hy[1:] - hy[:-1])/eps[:-1] + Pe[1:]/eps[:-1]        
    ex[source_point] += source(q,t0,tau)           
    if q % int(n/20*np.sqrt(epsilon))==0 or q+5>tot_time:
        drawplot(z, ex, hy, q)
