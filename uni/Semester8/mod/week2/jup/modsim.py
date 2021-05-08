import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate
import scipy.optimize

def plot_richtungsfeld(FUNC, n=10, tmin=0, tmax=5, xmin=0, xmax=10):

    t = np.linspace(tmin,tmax,n)
    u = np.linspace(xmax,xmin,n)
    f = np.zeros((n,n))
    
    
    for i in range(n):
        for j in range(n):
            f[j,i] = FUNC(t[i], u[j])

    plt.xlim((tmin-0.5,tmax+0.5))
    plt.ylim((xmin-0.5, xmax+0.5))
    plt.quiver(t,u,np.ones((n,n)),f)