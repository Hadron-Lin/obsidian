---
tags:
  - skill
---
# Basics
```python
import numpy as np
a=np.array([1,2,3],dtype='int16')
b=np.array([[9,8,7],[6,5,4]])
print(a)
print(b)
```

## 维度
```python
print(a.ndim)
print(b.ndim)
```

## 形状
```python
print(a.shape)
print(b.shape)
print(a.size)
print(b.size)
```


## 数据类型
```python
print(a.dtype)
print(b.dtype)
```


## 字节
```python
print(a.itemsize)
print(b.itemsize)
print(a.nbytes)
print(b.nbytes)
```
`nbytes`=`itemsize` $\times$ `size`


## full
```python
a=np.arange(1,37)  
b=a.reshape([4,9])  
print(b)  
c=np.full_like(b,23)  
print(c)  
d=np.full(b.shape,3)  
print(d)
```


## random
```python
a=np.random.rand(3,4)
print(a)

b=np.random.randint(2,9,size=[5,4])
print(b)
```


## 单位矩阵
```python
eye=np.identity(5)
print(eye)
```


## 重复
```python
a=np.array([[1,2,3]])
b=np.repeat(a,3,axis=0)
print(b)
```







