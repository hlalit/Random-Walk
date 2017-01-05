import numpy as np
import matplotlib.pyplot as plt 
import math as mt

from scipy.stats import norm
from scipy.stats import multivariate_normal

def gibbs(n,x):

    x[0,:] = [10,10]
    mu = np.array([0,0])
    sigma = np.matrix([[1,0.9],[0.9,1]])
    rho = float(0.9) 
    #setting the variance = 1 makes the math easy

    for i in range(1,n):
        x[i,0] = np.random.normal(rho*x[i-1,1],(1-rho*rho))
        x[i,1] = np.random.normal(rho*x[i,0],(1-rho*rho))

    plt.figure(2)    
    plt.plot(x[:,0],x[:,1],marker = 'o',color = 'r') 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()       
     
    return 
