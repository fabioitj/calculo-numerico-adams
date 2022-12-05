import numpy as np
import math 
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt # side-stepping mpl backend
import matplotlib.gridspec as gridspec # subplots
import warnings

def myfun_ty(t,y):
    return t-y

# Start and end of interval
b=2
a=0
# Step size
N=4
h=(b-a)/(N)
t=np.arange(a,b+h,h)
fig = plt.figure(figsize=(10,4))
plt.plot(t,0*t,'o:',color='red')
plt.xlim((0,2))
plt.title('Illustration of discrete time points for h=%s'%(h))

IC=1 # Intial condtion
y=(IC+1)*np.exp(-t)+t-1
fig = plt.figure(figsize=(6,4))
plt.plot(t,y,'o-',color='black')
plt.title('Exact Solution ')
plt.xlabel('time')

### Initial conditions
w=np.zeros(len(t))
w[0]=IC
w[1]=y[1] # NEEDED FOR THE METHOD

for k in range (1,N):
    w[k+1]=(w[k]+h/12.0*(5*t[k+1]+8*myfun_ty(t[k],w[k])-myfun_ty(t[k-1],w[k-1])))/(1+5*h/12) 

def plotting(t,w,y):
    fig = plt.figure(figsize=(10,4))
    plt.plot(t,y, 'o-',color='black',label='Exact')
    plt.plot(t,w,'s:',color='blue',label='Adams-Moulton')
    plt.xlabel('time')
    plt.legend()
    plt.show 

plotting(t,w,y)