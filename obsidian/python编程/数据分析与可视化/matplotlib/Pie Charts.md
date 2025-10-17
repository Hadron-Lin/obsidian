---
tags:
  - skill
---
# 基本语法
```python
from matplotlib import pyplot as plt  
# Language Popularity  
slices = [59219, 55466, 47544, 36443, 35917]  
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']  
plt.pie(slices,labels=labels)  
plt.title('My Awesome Pie Chart')  
plt.tight_layout()  
plt.show()
```

# 参数
## `wedgeprops`

`wedgeprops` 是 matplotlib 饼图中用于**控制饼图扇区(wedge)外观属性**的参数,可以自定义扇区的边框,颜色,样式等.

```python
from matplotlib import pyplot as plt  
# Language Popularity  
slices = [59219, 55466, 47544, 36443, 35917]  
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']  
plt.pie(slices,labels=labels,wedgeprops={'edgecolor':'black','linewidth': 2,'linestyle': '--','alpha':0.5,'fill':True})  
plt.title('My Awesome Pie Chart')  
plt.tight_layout()  
plt.show()
```

## `explode`

使图块从中分离
```python
from matplotlib import pyplot as plt  
# Language Popularity  
slices = [59219, 55466, 47544, 36443, 35917]  
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']  
explode=[0,0,0,0.1,0]  
plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'})  
plt.title('My Awesome Pie Chart')  
plt.tight_layout()  
plt.show()
```

## `autopct`

为每一块扇形标注数值
```python
from matplotlib import pyplot as plt  
# Language Popularity  
slices = [59219, 55466, 47544, 36443, 35917]  
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']  
explode=[0,0,0,0.1,0]  
plt.pie(slices,labels=labels,explode=explode,autopct='%1.2f%%',wedgeprops={'edgecolor':'black'})  
plt.title('My Awesome Pie Chart')  
plt.tight_layout()  
plt.show()
```

## `shadow`

显示阴影
```python
from matplotlib import pyplot as plt  
# Language Popularity  
slices = [59219, 55466, 47544, 36443, 35917]  
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']  
explode=[0,0,0,0.1,0]  
plt.pie(slices,labels=labels,explode=explode,autopct='%1.2f%%',shadow=True,wedgeprops={'edgecolor':'black'})  
plt.title('My Awesome Pie Chart')  
plt.tight_layout()  
plt.show()
```