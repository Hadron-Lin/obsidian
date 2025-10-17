---
tags:
  - skill
---
```python
from matplotlib import pyplot as plt  
  
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  
py_dev_y = [45372, 48876, 53850, 57287, 63016,  
            65998, 70003, 70000, 71496, 75370, 83640]  
  
js_dev_y = [37810, 43515, 46823, 49293, 53437,  
            56373, 62375, 66674, 68745, 68746, 74583]
```
# 基本语法
```python
plt.bar(age_x,py_dev_y) 
  
plt.title("Median Salary (USD) by Age")  
plt.xlabel("Ages")  
plt.ylabel("Median Salary (USD)")  
  
plt.tight_layout()  
  
plt.show()
```

**横向图表**
```python
plt.barh(age_x,py_dev_y) 
  
plt.title("Median Salary (USD) by Age")  
plt.ylabel("Ages")  
plt.xlabel("Median Salary (USD)")  
  
plt.tight_layout()  
plt.grid(True)
plt.show()
```


>[!tip] 引入numpy进行数据计较

```python restart=true
from matplotlib import pyplot as plt 
import numpy as np  
age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  
x_indexes=np.arange(len(age_x))  
width=0.25  
py_dev_y = [45372, 48876, 53850, 57287, 63016,  
            65998, 70003, 70000, 71496, 75370, 83640]  
js_dev_y = [37810, 43515, 46823, 49293, 53437,  
            56373, 62375, 66674, 68745, 68746, 74583]  
dev_y = [17784, 16500, 18012, 20628, 25206,  
         30252, 34368, 38496, 42000, 46752, 49320]  
plt.bar(x_indexes-width,py_dev_y,width=width,label='python')  
plt.bar(x_indexes,js_dev_y,width=width,label='java')  
plt.bar(x_indexes+width,dev_y,width=width,label='all')  
  
plt.xticks(ticks=x_indexes,
           labels=age_x)
  
plt.title("Median Salary (USD) by Age")  
plt.xlabel("Ages")  
plt.ylabel("Median Salary (USD)")  
  
plt.legend()  
  
plt.tight_layout()  
  
plt.show()
```