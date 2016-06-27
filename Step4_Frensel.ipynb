%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt

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
    plt.savefig("step3-at-time-%i.png"%q, fmt='png')
    plt.draw()
    
def draw_error_plot(eps2, er_ar1, er_ar2, er_ar3):
    fig = plt.figure()
    plt.title('Error vs. epsilon2')
    plt.grid(True)
    plt.xlabel(u'epsilon2')
    plt.ylabel(u'error level, %')
    ax = fig.add_subplot(111)
    ax.plot(eps2, er_ar1, '-', color = 'black', linewidth=2, label=u'Eps1 = 1')
    ax.plot(eps2, er_ar2, '-', color = 'blue', linewidth=2, label=u'Eps1 = 500')
    ax.plot(eps2, er_ar3, '-', color = 'red', linewidth=2, label=u'Eps1 = 1000')
    #fig.plot(eps2, er_ar1, '-', color = 'green,', linewidth=2, label=u'Eps1 = 1000')
    plt.legend()
    plt.savefig("plot.png", fmt='png')
    plt.draw()

def frensel(epsilon1, epsilon2):
    n = 3600 #number of points
    #epsilon = 25
    if epsilon2 > epsilon1:
        epsilon = epsilon2
    else:
        epsilon = epsilon1
    tau = (n//400)*np.sqrt(epsilon) #puls width
    t0 = 10.0*tau #delay of the source
    tot_time = int(n*np.sqrt(epsilon)+t0)
    source_point = n//16

    pml_width=20 #PML width
    #eps = epsilon*np.ones(n)

    dx = 1
    R0 = 10**(-6)
    m = 4
    
    n1 = np.sqrt(epsilon1)
    n2 = np.sqrt(epsilon2)
    eps = np.ones(n)
    eps[int(n//2):] = epsilon2
    eps[:int(n//2)] = epsilon1
    #Frensel equations:
    R = np.abs(((n2-n1)/(n2+n1))**2)
    T = 4*n1*n2/((n1+n2)**2)
    frensel_ratio = T/R
    
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
    E, Et, Er = 0, 0, 0
    H, Ht, Hr = 0, 0, 0
    T1 = int((n//2 - source_point)*n1+0.5*t0)
    T2 = int(T1 + t0)
    for q in range(T1):
        Pm[:-1] = Bm[:-1]*Pm[:-1] + Am[:-1]*(ex[1:] - ex[:-1])
        hy[:-1] += ex[1:] - ex[:-1] + Pm[:-1]
        Pe[1:] = Be[1:]*Pe[1:] + Ae[1:]*(hy[1:] - hy[:-1])
        ex[1:] += (hy[1:] - hy[:-1])/eps[:-1] + Pe[1:]/eps[:-1]
        ex[source_point] += source(q,t0,tau)
        #if q % int(n/20*np.sqrt(epsilon))==0 or q+5>tot_time:
    #drawplot(z, ex, hy, q)
    for nn in range(n):
        if ex[nn]>E:
            E = ex[nn]
        if ex[nn]<0 and -ex[nn]>E:
            E = -ex[nn]
        if hy[nn]>H:
            H = hy[nn]
        if hy[nn]<0 and -hy[nn]>H:
            H = -hy[nn]    
    for q in range(T1, T2):
        Pm[:-1] = Bm[:-1]*Pm[:-1] + Am[:-1]*(ex[1:] - ex[:-1])
        hy[:-1] += ex[1:] - ex[:-1] + Pm[:-1]
        Pe[1:] = Be[1:]*Pe[1:] + Ae[1:]*(hy[1:] - hy[:-1])
        ex[1:] += (hy[1:] - hy[:-1])/eps[:-1] + Pe[1:]/eps[:-1]
        ex[source_point] += source(q,t0,tau)    
        #if q == tot_time//4:
        #    for nn in range(n):
        #        if ex[nn]>E:
        #            E = ex[nn]
        #if q % int(n/20*np.sqrt(epsilon))==0 or q+5>tot_time:
    #drawplot(z, ex, hy, q)
    for nn in range(int(n//2)):
        if ex[nn]>Er:
            Er = ex[nn]
        if ex[nn]<0 and -ex[nn]>Er:
            Er = -ex[nn]
        if hy[nn]>Hr:
            Hr = hy[nn]
        if hy[nn]<0 and -hy[nn]>Hr:
            Hr = -hy[nn] 
    for nn in range(int(n//2),n):
        if ex[nn]>Et:
            Et = ex[nn]
        if ex[nn]<0 and -ex[nn]>Et:
            Et = -ex[nn]
        if hy[nn]>Ht:
            Ht = hy[nn]
        if hy[nn]<0 and -hy[nn]>Ht:
            Ht = -hy[nn] 
    #print('E  = ',E)
    #print('Er = ',Er)
    #print('Et = ',Et)
    #print('H  = ',H)
    #print('Hr = ',Hr)
    #print('Ht = ',Ht)
    #print('E*H  = ',E*H)
    #print('(E*H)r = ',Er*Hr)
    #print('(E*H)t = ',Et*Ht)
    #print()
    #print('(E*H)r = ',E*H*R)
    #print('(E*H)t = ',E*H*T)
    fdtd_t = (Et*Ht)/(E*H)
    fdtd_r = (Er*Hr)/(E*H)
    fdtd_ratio = fdtd_t/fdtd_r
    error = np.abs((fdtd_ratio-frensel_ratio)/frensel_ratio)*100
    #print('For eps1 = ',epsilon1,' and eps2 = ',epsilon2,':')
    #print('по FDTD: R = ',fdtd_r,', T = ',fdtd_t,', T/R = ',fdtd_ratio)
    #print('R = ',fdtd_r,', T = ',fdtd_t,', T/R = ',fdtd_ratio)
    #print('по Френелю: R = ',R,', T = ',T,', T/R = ',frensel_ratio)
    #print('R = ',R,', T = ',T,', T/R = ',frensel_ratio)
    #print()
    #print('For eps1 = ',epsilon1,' and eps2 = ',epsilon2,':')
    #print('FDTD_T/R = ',fdtd_ratio)
    #print('Frensel_T/R = ',frensel_ratio)
    #print('Error = ',error,'%')
    #print()
    #print('(E*H)t+(E*H)r = ',Et*Ht+Er*Hr)
    return error

eps2_max = 1000
eps_n = 10
eps2 = np.linspace(1,eps2_max,eps_n)
er_ar1 = np.zeros(eps_n)
er_ar2 = np.zeros(eps_n)
er_ar3 = np.zeros(eps_n) 
#print(eps2[0])
#print(er_ar1)
a = 0
a_max = 3*eps_n
for nn in range(eps_n):
    if not eps2[nn] == 1:
        er_ar1[nn] = frensel(1,eps2[nn])
        a += 1
        print(a/a_max*100,"% finished")
    if not eps2[nn] == 500:
        er_ar2[nn] = frensel(500,eps2[nn])
        a += 1
        print(a/a_max*100,"% finished")
    if not eps2[nn] == 1000:
        er_ar3[nn] = frensel(1000,eps2[nn])
        a += 1
        print(a/a_max*100,"% finished")
draw_error_plot(eps2, er_ar1, er_ar2, er_ar3)
#er = frensel(1,1000)
#print(er)
#epsilon1, epsilon2 = 8,2
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 3,5
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 1,9
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 10,1
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 10,12
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 12,10
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 16,25
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 25,16
#frensel(epsilon1, epsilon2)
#epsilon1, epsilon2 = 100,200
#frensel(epsilon1, epsilon2)
