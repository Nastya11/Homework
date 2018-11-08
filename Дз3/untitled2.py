# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:19:54 2018

@author: Tom
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from scipy import stats

w = 100
h = 50

def t_ij(x, tau1, tau2, mu1, mu2, sigma1, sigma2):
    """T_ij(x, theta)"""
    p_in1 = (stats.norm.pdf(x, loc = mu1, scale = sigma1))*(1/np.sqrt(2*np.pi*sigma1))
    p_in2 = (stats.norm.pdf(x, loc = mu2, scale = sigma2))*(1/np.sqrt(2*np.pi*sigma2))
    p_un = 1/ (w*h)
    p = tau1 * p_in1 + tau2 * p_in2 + (1-tau1-tau2) * p_un
    t_in1 = tau1 * p_in1 / p
    t_in2 = tau2 * p_in2 / p
    t_un = (1 - tau1 - tau2) * p_un / p 
    return t_in1, t_in2, t_un

def update_theta(x, tau1, tau2, mu1, mu2, sigma1, sigma2):
    """Iterate theta"""
    t_n1, t_n2, t_u = t_ij(x, tau1, tau2, mu1, mu2, sigma1, sigma2)
    tau1 = np.sum(t_n1) / np.sum(t_n1+t_n2+t_u)
    tau2 = np.sum(t_n2) / np.sum(t_n1+t_n2+t_u)
    mu1 = np.sum(t_n1 * x) /  np.sum(t_n1)
    mu2 = np.sum(t_n2 * x) /  np.sum(t_n2)
    sigma1 = np.sqrt(np.sum(t_n1 * (x - mu1)**2) /  np.sum(t_n1))
    sigma1 = np.sqrt(np.sum(t_n1 * (x - mu1)**2) /  np.sum(t_n1))
    return tau1, tau2, mu1, sigma1, mu2, sigma2

def em_complicated_function(x, tau1, tau2, mu1, sigma1, mu2, sigma2, rtol=1e-3):
    """tau, mu, sigma are initiial astimations, returns theta"""
    new = (tau1, tau2, mu1, sigma1, mu2, sigma2)
    rtol = 1e-3
    while True:
        old = new
        new = update_theta(x, *old)
        if np.allclose(new, old, rtol = rtol, atol = 0):
            break
    return new

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.vizier import Vizier

center_coord = SkyCoord('02h21m00s +57d07m42s')
vizier = Vizier(
    column_filters={'Bmag': '<13'},  # число больше — звёзд больше
    row_limit=10000
)
stars = vizier.query_region(
    center_coord,
    width=1.5 * u.deg,
    height=1.5 * u.deg,
    catalog='USNO-A2.0',
)[0]
ra = stars['RAJ2000']._data  # прямое восхождение, аналог долготы
dec = stars['DEJ2000']._data  # склонение, аналог широты
x1 = (ra - ra.mean()) * np.cos(dec / 180 * np.pi/2)
x2 = dec
s = (np.max(x1)-np.min(x1))*(np.max(x2)-np.min(x2))
print (s)
result = em_complicated_function([x1, x2], 0.7,0.3, 0.1, 0.1, 0.3, 0.2, rtol=1e-3)
print(result)
plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.plot(x1,x2)
plt.grid()
