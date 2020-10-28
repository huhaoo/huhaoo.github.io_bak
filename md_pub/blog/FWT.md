---
title: FWT
date: 2019-09-28 09:57:27
tags:
- FWT
- math
mathjax: on
---

 ![math](https://render.githubusercontent.com/render/math?math=) 

<!--more-->

记 ![math](https://render.githubusercontent.com/render/math?math=A_0) 为 ![math](https://render.githubusercontent.com/render/math?math=A_%7B0%5Cdots2%5E%7Bn-1%7D-1%7D) , ![math](https://render.githubusercontent.com/render/math?math=A_1) 为 ![math](https://render.githubusercontent.com/render/math?math=A_%7B2%5E%7Bn-1%7D%5Cdots2%5En-1%7D) ， ![math](https://render.githubusercontent.com/render/math?math=B%2CC) 同理

我们不妨记对常数运算和对多项式加减为各位分别处理

我们可以发现 ![math](https://render.githubusercontent.com/render/math?math=%5Cmathrm%7Bopt%7D) 和 ![math](https://render.githubusercontent.com/render/math?math=%2B) 有结合率（类似 ![math](https://render.githubusercontent.com/render/math?math=%5Ctimes) ）

####  ![math](https://render.githubusercontent.com/render/math?math=%5Cmathrm%7Bor%7D) 



![math](https://render.githubusercontent.com/render/math?math=C_0%3DA_0%7E%5Cmathrm%7Bor%7D%7EB_0%5C%5C%5C%5C%0AC_1%3DA_0%7E%5Cmathrm%7Bor%7D%7EB_1%2BA_1%7E%5Cmathrm%7Bor%7D%7EB_0%2BA_1%7E%5Cmathrm%7Bor%7D%7EB_1%5C%5C%5C%5C%0A%3D%28A_0%2BA_1%29%7E%5Cmathrm%7Bor%7D%7E%28B_0%2BB_1%29-C_0)



####  ![math](https://render.githubusercontent.com/render/math?math=%5Cmathrm%7Band%7D) 



![math](https://render.githubusercontent.com/render/math?math=C_1%3DA_1%7E%5Cmathrm%7Band%7D%7EB_1%5C%5C%5C%5C%0AC_0%3DA_0%7E%5Cmathrm%7Band%7D%7EB_0%2BA_0%7E%5Cmathrm%7Band%7D%7EB_1%2BA_1%7E%5Cmathrm%7Band%7D%7EB_0%5C%5C%5C%5C%0A%3D%28A_0%2BA_1%29%7E%5Cmathrm%7Band%7D%7E%28B_0%2BB_1%29-C_1)



####  ![math](https://render.githubusercontent.com/render/math?math=%5Cmathrm%7Bxor%7D) 



![math](https://render.githubusercontent.com/render/math?math=C_0%3DA_0%7E%5Cmathrm%7Bxor%7D%7EB_0%2BA_1%7E%5Cmathrm%7Bxor%7D%7EB_1%5C%5C%5C%5C%0AC_1%3DA_0%7E%5Cmathrm%7Bxor%7D%7EB_1%2BA_1%7E%5Cmathrm%7Bxor%7D%7EB_0)



各分两个，直接搞的话复杂度变成了暴力

然而这就有一个显然的套路

记


![math](https://render.githubusercontent.com/render/math?math=X%3D%28A_0%2BA_1%29%7E%5Cmathrm%7Bxor%7D%7E%28B_0%2BB_1%29%5C%5C%5C%5C%0AY%3D%28A_0-A_1%29%7E%5Cmathrm%7Bxor%7D%7E%28B_0-B_1%29%5C%5C%5C%5C%0AC_0%3D%5Cdfrac%7BX%2BY%7D2%2CC_1%3D%5Cdfrac%7BX-Y%7D2)



#### 复杂度

有 ![math](https://render.githubusercontent.com/render/math?math=f%282%5En%29%3D2f%282%5E%7Bn-1%7D%29%2BO%282%5En%29) 

也就是 ![math](https://render.githubusercontent.com/render/math?math=O%28n2%5En%29) （在数据规模 ![math](https://render.githubusercontent.com/render/math?math=2%5En) 情况下）
