---
tags:
  - skill
---
## 应用场景
统计数据的频率
# 基本语法
```python
from matplotlib import pyplot as plt  
import numpy as np  
  
data=np.random.normal(76,7,1000000)  

plt.hist(data,bins=1000)  
  
plt.xlabel('scores')  
plt.ylabel('Number of People')  
plt.title('the Distribution of Scores')

plt.grid(True)

plt.show()
```

>[!tip] 加入线条

```python
from matplotlib import pyplot as plt  
import numpy as np  
  
data = np.random.normal(75, 5, 1000000)  
  
plt.hist(data, bins=1000)  
  
median_score=60  
  
plt.axvline(median_score,color='red',label='Passing Score')  
  
plt.xlabel('scores')  
plt.ylabel('Number of People')  
plt.title('the Distribution of Scores')  
plt.legend()  
  
plt.grid(True)  
  
plt.show()
```