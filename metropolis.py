import numpy as np
import matplotlib.pyplot as plt 
import math as mt

from scipy.stats import norm
from scipy.stats import multivariate_normal

def metro(n,x):

    u = float
    x[0,:] = [10,10]                        #initial guess 
    mu = np.array([0,0])                    #mean of source matrix 
    sigma = np.matrix([[1,0.9],[0.9,1]])    #covariance matrix of source matrix
    
    for i in range(0,n-1):
        
        u = np.random.uniform(0,1)
        x_c = np.random.multivariate_normal(x[i,:],sigma)  
        m = min(1,multivariate_normal.pdf(x_c,mu,sigma)/multivariate_normal.pdf(x[i,:],mu,sigma))
        
        if u < m:
            x[i+1,:] = x_c
        else:
            x[i+1,:] = x[i,:]
    
    plt.figure(1)
    plt.plot(x[:,0],x[:,1],marker = 'o',color = 'r') 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
                      
    return 

        


