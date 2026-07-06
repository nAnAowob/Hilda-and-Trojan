import pandas as pd
from sympy import symbols, solve
df = pd.read_csv(r'CoMat_finalCode/CoMatDataDummy.csv')
#rf = pd.read_csv(r'/Users/chompunick/Dropbox/Mac/Desktop/CoMat/CoMat_finalCode/coordinate.csv')
import matplotlib.pyplot as plt
import sympy as sp
import math as mt
from math import sin,cos,tan,atan
import numpy as np
import csv
from scipy.stats import gaussian_kde
#plt.style.use('seaborn-white')
def find_densest_point_q1(x, y, z):
    densest_point = (x[0], y[0])
    densest_density = z[0]
    
    for i in range(len(x)):
        if y[i] > 0:
            if z[i] > densest_density:
                densest_density = z[i]
                densest_point = (x[i], y[i])
        
    return densest_point
def find_densest_point_q3(x, y, z):
    densest_point = (x[0], y[0])
    densest_density = z[0]
    
    for i in range(len(x)):
        if x[i] < 0 and y[i] < 0:
            if z[i] > densest_density:
                densest_density = z[i]
                densest_point = (x[i], y[i])
        
    return densest_point

def find_densest_point_q4(x, y, z):
    densest_point = (x[0], y[0])
    densest_density = z[0]
    
    for i in range(len(x)):
        if x[i] > 0 and y[i] < 0:
            if z[i] > densest_density:
                densest_density = z[i]
                densest_point = (x[i], y[i])
        
    return densest_point


e = df.e
a1 = df.a
M1 = df.M
N1 = df.Node
i1 = df.Incl
w1 = df.Peri
fig = plt.figure()
#ax = plt.axes(projection="2d")
i = [0 for I in range(0,len(e),1)]
N = [0 for I in range(0,len(e),1)]
M = [0 for I in range(0,len(e),1)]
w = [0 for I in range(0,len(e),1)]

x_cart = [0 for I in range(0,len(e),1)]
y_cart = [0 for I in range(0,len(e),1)]
z_cart = [0 for I in range(0,len(e),1)]

q2 = [0 for I in range(0,len(e),1)]
q3 = [0 for I in range(0,len(e),1)]
q4 = [0 for I in range(0,len(e),1)]

for c in range(0,len(e),1):
    i[c] = mt.radians(i1[c])
    #a[c] = a[c]*149597870700
    N[c] = mt.radians(N1[c])
    M[c] = mt.radians(M1[c])
    w[c] = mt.radians(w1[c])
    E = sp.symbols('E')
    s = sp.nsolve(E-e[c]*sp.sin(E)-M[c],E,1)
    s=float(s)
    v = 2*mt.atan(mt.sqrt((1+e[c])/(1-e[c]))*(mt.sin(s/2)/mt.cos(s/2)))
    r = a1[c]*(1-e[c]**2)/(1+e[c]*mt.cos(v))
    x_ecl = r * ( cos(N[c]) * cos(v+w[c]) - sin(N[c]) * sin(v+w[c]) * cos(i[c]) )
    y_ecl = r * ( sin(N[c]) * cos(v+w[c]) + cos(N[c]) * sin(v+w[c]) * cos(i[c]) )
    z_ecl = r * ( sin(v+w[c]) * sin(i[c]) )
    x_cart[c] = x_ecl * mt.cos(e[c]) - y_ecl * mt.sin(e[c])
    y_cart[c] = x_ecl * mt.sin(e[c]) + y_ecl * mt.cos(e[c])
    z_cart[c] = z_ecl
'''    with open('s_coordinate.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([x_cart[c],y_cart[c]],z_cart[c])
'''
xy = np.vstack([x_cart,y_cart])
z = gaussian_kde(xy)(xy)
x1,y1 = find_densest_point_q1(x_cart,y_cart,z)
print(x1,y1)
x3,y3 = find_densest_point_q3(x_cart,y_cart,z)
print(x3,y3)
x4,y4 = find_densest_point_q4(x_cart,y_cart,z)
print(x4,y4)

fig, ax = plt.subplots()
plt.scatter(x_cart,y_cart,c=z,s=5,cmap='rainbow')
plt.colorbar()
plt.show()
#for c in range(0,len(e),1):
