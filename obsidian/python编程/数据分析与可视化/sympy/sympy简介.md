---
tags:
  - definition
---
sympy主要用来符号计算,比numpy更加精确,因为sympy纯理论推导,最精确.而numpy是数值计算.
# 实际工作流
**step1**:sympy进行数理推演
**step2**:numpy进行数值计算
**step3**:matplotlib进行可视化


```python

import sympy as sp  
import numpy as np  
import matplotlib.pyplot as plt  
  
   
x,y,z,k,q,l=sp.symbols('x y z k q l')  
  
U=k*q/sp.sqrt((x-l/2)**2+y**2)-k*q/sp.sqrt((x+l/2)**2+y**2)  
  
Ex=-sp.diff(U,x)  
Ey=-sp.diff(U,y)  
  
U_num=sp.lambdify((x,y),U.subs([(k,8.99e9),(q,1),(l,2)]),'numpy')  
  
Ex_num=sp.lambdify((x,y),Ex.subs([(k,8.99e9),(q,1),(l,2)]),'numpy')  
Ey_num=sp.lambdify((x,y),Ey.subs([(k,8.99e9),(q,1),(l,2)]),'numpy')  
   
X,Y=np.meshgrid(np.linspace(-5,5,100),np.linspace(-5,5,100))  
  
U_vals=U_num(X,Y)  
  
Ex_vals=Ex_num(X,Y)  
Ey_vals=Ey_num(X,Y)  
 
fig=plt.figure()  
ax1=fig.add_subplot(2,1,1,projection='3d')  
ax1.plot_surface(X,Y,U_vals)  
ax1.set_xlabel('x')  
ax1.set_ylabel('y')  
ax1.set_zlabel('U')  
  
  
ax2=fig.add_subplot(2,1,2)  
ax2.streamplot(x=X,y=Y,u=Ex_vals,v=Ey_vals)  
ax2.set_xlabel('x')  
ax2.set_ylabel('y')  
ax2.scatter([-1,1],[0,0],c=['blue','red'],s=100,marker='o')  
  
plt.show()
```