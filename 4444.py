#-*-coding:utf8-*-
#user:brian
#created_at:2018/7/23 16:17
# file: 4444.py
#location: china chengdu 610000
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy import stats
import statsmodels.api as sm
X_train=[[1,2,3],[4,5,6],[7,8,9]]
y_train=[1,2,3]
mod = sm.OLS(y_train, X_train)
res = mod.fit()
print(res.summary())
linreg = LinearRegression()

model=linreg.fit(X_train, y_train)
print (model)
print (linreg.intercept_)
print (linreg.coef_)

import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 5+2*x+3*x**2-0.5*x**3

def fund(x):
    return 200-10*x

#np.linspace()取x的值
x=np.linspace(-10,10,50)
y=func(x)
y1=fund(x)

fig,ax=plt.subplots()
plt.plot(x,y,'r-o',lw=1)
plt.plot(x,y1,'g-*',lw=1)
#plt.ylim(ymin=0)  控制y轴现实范围
a,b=-10,3
xf=x[np.where((x>a)&(x<b))]
#plt.fill_between(xf),在xf范围内
# #曲线1：np.zeros(len(xf))与曲线2：func(xf)之间的区域
# #np.zeros()从零开始，np.ones()从1开始，np.ones()*20从20开始 #plt.fill_between(xf, np.zeros(len(xf)), func(xf), color='blue', alpha=.25)
# #两条曲线之间的区域
plt.fill_between(xf,func(xf),fund(xf),color='blue',alpha=0.25)
plt.show()
plt.close()

for i in range(5):
    print(i)
