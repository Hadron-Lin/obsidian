---
tags:
  - element
aliases:
previous:
  - "[[MOSFET工作原理]]"
next:
  - 
links:
  -
---

# 基础逻辑
N-type:$V_{G}>V_{S}$
P-type:$V_{G}<V_{S}$
**原因**:![[MOSFET工作原理#^a20384]]

![[Pasted image 20251024133845.png|500]]

# COMS逻辑门
>[!important] CMOS的核心是对偶性
>保证上下电路结构符合**对偶性**:
>- 串联-并联

>[!success] 对偶结构设计意义
>- 理论上零功率消耗(因为非开即断,没有静态电流)
>- 构建了规整的数字电路

>[!tip] 利用对偶特性推导输出表达式
>只用看上面部分即可,如下列推导

## 反相器
![[Pasted image 20251024135429.png|200]]
$$
\begin{align}
V_{out}=\overline{V_{in}}
\end{align}
$$
## 与非门
![[Pasted image 20251024135726.png|200]]
$$
\begin{align}
Z=\overline{A}+\overline{B}=\overline{AB}
\end{align}
$$

## 或非门
![[Pasted image 20251024140051.png|200]]
$$
\begin{align}
P=\overline{A}\cdot \overline{B}
\end{align}
$$



## 与或非门
![[Pasted image 20251024140951.png|200]]
$$
\begin{align}
Z=(\overline{A}+\overline{B})\cdot(\overline{C}+\overline{D})=\overline{AB+CD}
\end{align}
$$

## 或与非门
![[Pasted image 20251024141023.png|200]]
$$
\begin{align}
\overline{A}\cdot\overline{B}+\overline{C}\cdot \overline{D}=\overline{(A+B)\cdot(C+D)}
\end{align}
$$
## 非反相
### 非反相门
![[Pasted image 20251024142330.png|300]]
就是两个反相器
>[!important] 逻辑反相是免费的
>即在电路中实现逻辑反相的成本极低,可以忽略.

### 与门
直接在**与非门**后面加个反相器就可以了
![[Pasted image 20251024144602.png|300]]


---
# 例题

![[Pasted image 20251024184003.png|650]]
![[Pasted image 20251024183932.png|]]
$$
\begin{align}
F=\overline{AB+C}=(\overline{A}+\overline{B})\cdot \overline{C}
\end{align}
$$

---

![[Pasted image 20251024184709.png|650]]
$$
\begin{align}
高态:4.9-3.5=1.4V \\
低态:1.5-0.1=1.4V
\end{align}
$$







