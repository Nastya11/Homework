# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:33:20 2018

@author: Tom
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from scipy import stats

def data_generation():
    tau = 0.5
    mu1 = 0.5
    sigma1 = 0.2
    mu2 = 0.8
    sigma2= 0.6
    n=10000
    
    x_n = stats.norm.rvs(loc=mu1, scale=sigma1, size=int(tau*n))
    x_u = stats.norm.rvs(loc=mu2, scale=sigma2, size=int((1-tau)*n))
    x = np.concatenate((x_u, x_n))
    return x
#minimize

# def fun(x, args*)
# x - np.ndarray - оптимизируемые параметры
# *args = (a,b,c,d) - другие параметры
def phi(params,x):
    tau, mu1, sigma1, mu2, sigma2=params
    p1 = stats.norm.pdf(x, loc = mu1, scale = sigma1)
    p2 = stats.norm.pdf(x, loc = mu2, scale = sigma2)
    return -np.sum(np.log(tau*p1 +(1-tau)*p2))

def main():
    x = data_generation()
    #plt.hist(x, bins=100)
    result = optimize.minimize(phi, x0 = [0.7, 0.1, 0.1, 0.3, 0.2], args = (x), tol=1e-3)
    print(result)
    

if __name__ == '__main__':
    main()