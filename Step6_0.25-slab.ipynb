%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt
from matplotlib import patches


n = 1800 #number of points
epsilon_m = 1 #eps of the media
epsilon_s = 4 #eps of the slab
lamda = int(np.pi*2*(n//50))
tau = n//100
print("lamda = ",lamda)
t0 = 10.0*tau #delay of the source
tot_time = int(n*np.sqrt(epsilon_s)+t0)
source_point = n//4

pml_width=20 #PML width
m = 4  
R0 = 10**(-6)
dx = 1
Smax = -(m+1)*np.log(R0)/2/(pml_width*dx)
f = 4    #for lamda/2
X = int(lamda*n1/n2/f)

print("epsilon_m = ",epsilon_m)
print("epsilon_s = ",epsilon_s)
n_m = np.sqrt(epsilon_m)
n_s = 1.0/X*lamda*n_m/f
epsilon_s = n_s**2 #corrected eps of the slab
print("new epsilon_s = ",epsilon_s)
eps = epsilon_m*np.ones(n)
eps[n//2 - X//2:n//2 + X//2] = epsilon_s
reps= epsilon_m*np.ones(n)
  
ex=np.zeros(n)
hy=np.zeros(n)
rex=np.zeros(n)
rhy=np.zeros(n)
z=np.linspace(0,n-1,n)

def source(t, t0, tau):
    amp = math.exp(-(t-t0)**2/(2.0 * tau**2))   
    if t > t0:
        amp = 1.0
    return amp/np.sqrt(epsilon_s)*np.sin(2*np.pi*t/lamda)

def drawplot(z, ex, rex, q):
    s1 = patches.Rectangle((n//2 - X//2, -100), X, 200.0, zorder=0, color='blue',alpha = 0.2)
    s2 = patches.Rectangle((n//2 - X//2, -100), X, 200.0, zorder=0, color='blue',alpha = 0.2)
    fig = plt.figure()
    plt.title("After t=%i"%q)
    plt.grid(True)
    plt.xlabel(u'Coordinate z')
    plt.ylabel(u'Function')
    ax = fig.add_subplot(211)
    ax.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    ax.plot(z, rex, '--', color='red', linewidth=2, label=u'rEx')
    plt.legend()
    ax.add_patch(s1)
    bx = fig.add_subplot(212)
    bx.plot(z, ex-rex, '-', color='blue', linewidth=2, label=u'Ex-rEx')
    plt.legend()
    bx.add_patch(s2)
    plt.savefig("step6-at-time-%i.png"%q, fmt='png')
    plt.draw()
    
ex = np.zeros(n)
rex = np.zeros(n)
hy = np.zeros(n)
rhy = np.zeros(n)
z=np.linspace(0,n-1,n)
Se = np.zeros(n)
Sm = np.zeros(n)
Pe = np.zeros(n)
Pm = np.zeros(n)
rPe = np.zeros(n)
rPm = np.zeros(n)

for nn in range(int(pml_width)):
    Se[nn+1] = Smax*((pml_width-nn-0.5)/pml_width)**m
    Sm[nn] = Smax*((pml_width-nn)/pml_width)**m
    Se[n-1-nn] = Smax*((pml_width-nn-0.5)/pml_width)**m  
    Sm[n-1-nn] = Smax*((pml_width-nn)/pml_width)**m
    
Ae = np.exp(-Se) - 1
Be = np.exp(-Se) 
Am = np.exp(-Sm) - 1
Bm = np.exp(-Sm) 

for q in range(tot_time):
    Pm[:-1] = Bm[:-1]*Pm[:-1] + Am[:-1]*(ex[1:] - ex[:-1])
    hy[:-1] += ex[1:] - ex[:-1] + Pm[:-1]
    rPm[:-1] = Bm[:-1]*rPm[:-1] + Am[:-1]*(rex[1:] - rex[:-1])
    rhy[:-1] += rex[1:] - rex[:-1] + rPm[:-1]
    
    Pe[1:] = Be[1:]*Pe[1:] + Ae[1:]*(hy[1:] - hy[:-1])
    ex[1:] += (hy[1:] - hy[:-1])/eps[:-1] + Pe[1:]/eps[:-1]        
    ex[source_point] += source(q,t0,tau)    
    rPe[1:] = Be[1:]*rPe[1:] + Ae[1:]*(rhy[1:] - rhy[:-1])
    rex[1:] += (rhy[1:] - rhy[:-1])/reps[:-1] + rPe[1:]/reps[:-1]        
    rex[source_point] += source(q,t0,tau)         
    if q % int(n/20*np.sqrt(epsilon_s))==0 or q+5>tot_time:
        drawplot(z, ex, rex, q)
