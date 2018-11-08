# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:33:04 2018

@author: Tom
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:12:05 2018

@author: Tom
"""

"""Смесь нормальных распределений"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 0
b = 1

def data_generation():
    tau = 0.5
    mu1 = 0.5
    sigma1 = 0.2
    mu2 = 0.8
    sigma2 = 0.6
    n = 10000
    
    x_n = stats.norm.rvs(loc=mu1, scale=sigma1, size=int(tau*n))
    x_u = stats.norm.rvs(loc=mu2, scale=sigma2, size=int((1-tau)*n))
    x = np.concatenate((x_u, x_n))
    return x

def t_ij(x, tau, mu1, sigma1, mu2, sigma2):
    """T_ij(x, theta)"""
    p_in = stats.norm.pdf(x, loc = mu1, scale = sigma1)
    p_iu = stats.norm.pdf(x, loc = mu2, scale = sigma2)
    p = tau * p_in + (1-tau) * p_iu
    t_in = tau * p_in / p
    t_iu = (1-tau) * p_iu / p
    return t_in, t_iu

def update_theta(x, tau, mu1, sigma1, mu2, sigma2):
    """Iterate theta"""
    t_n, t_u = t_ij(x, tau, mu1, sigma1, mu2, sigma2)
    tau = np.sum(t_n) / x.size
    mu1 = np.sum(t_n * x) /  np.sum(t_n)
    mu2 = np.sum(t_u * x) /  np.sum(t_u)
    sigma1= np.sqrt(np.sum(t_n * (x - mu1)**2) /  np.sum(t_n))
    sigma2 = np.sqrt(np.sum(t_u * (x - mu2)**2) /  np.sum(t_u))
    return tau, mu1, sigma1, mu2, sigma2

def em_double_gauss(x,  tau, mu1, sigma1, mu2, sigma2, rtol=1e-3):
    """tau, mu, sigma are initiial astimations, returns theta"""
    new = ( tau, mu1, sigma1, mu2, sigma2)
    while True:
        old = new
        new = update_theta(x, *old)
        if np.allclose(new, old, rtol = rtol, atol = 0):
            break
    return new
    
def main():
    x = data_generation()
    plt.hist(x, bins=100)
    tau, mu1, sigma1, mu2, sigma2 = 0.7, 0.1, 0.1, 0.3, 0.2
    tau, mu1, sigma1, mu2, sigma2= em_double_gauss(x,  tau, mu1, sigma1, mu2, sigma2)
    print ( tau, mu1, sigma1, mu2, sigma2)
    
if __name__ == '__main__':
    main() 
