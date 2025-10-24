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

>[!question] 对偶结构设计意义


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
P=\overline{A}+\overline{B}=\overline{AB}
\end{align}
$$

## 或非门
![[Pasted image 20251024140051.png|200]]
$$
\begin{align}
P=\overline{A}\cdot \overline{B}\cdot(\overline{A}\cdot \overline{B})
\end{align}
$$

>[!question] 有没有规范的推导
>对偶结构特性



## 与或非门
![[Pasted image 20251024140951.png|200]]

## 或与非门
![[Pasted image 20251024141023.png|200]]

## 非反相
### 非反相门
![[Pasted image 20251024142330.png|300]]
就是两个反相器
>[!important] 逻辑反相是免费的
>即在电路中实现逻辑反相的成本极低,可以忽略.

### 与门
直接在**与非门**后面加个反相器就可以了


