---
tags:
  - skill
---
## 应用场景
直观地体现两个变量之间是否具有关系

# 基本语法
```python
from matplotlib import pyplot as plt  
import numpy as np  
  
dx=np.random.randint(-100,200,1000)  
x=np.arange(1000)+dx  
dy=np.random.randint(-30,200,1000)  
y=np.arange(1000)+dy  
  
plt.scatter(x,y)  
plt.show()
```

## 参数
### `s`

```python
from matplotlib import pyplot as plt  
import numpy as np  
  
dx=np.random.randint(-100,200,1000)  
x=np.arange(1000)+dx  
dy=np.random.randint(-30,200,1000)  
y=np.arange(1000)+dy  
  
scatter = plt.scatter(x, y, s=80)  
plt.show()
```

### `marker`

#### 常用图形
+
x
D(菱形)
^(三角形)
s(方形)
.(点)

```python
from matplotlib import pyplot as plt  
import numpy as np  
  
dx=np.random.randint(-100,200,1000)  
x=np.arange(1000)+dx  
dy=np.random.randint(-30,200,1000)  
y=np.arange(1000)+dy  
  
scatter = plt.scatter(x, y, marker='+')  
plt.grid(True)
plt.show()
```

