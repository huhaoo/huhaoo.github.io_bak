若 ![math](https://www.zhihu.com/equation?tex=g%28f%28x%29%29%3Dx) ，则称它们互为复合逆（即反函数）。

（拓展形式）Lagrange反演即：


![math](https://www.zhihu.com/equation?tex=%5Bx%5En%5Dh%28g%28x%29%29%3D%5Cdfrac%201n%5Bx%5E%7Bn-1%7D%5Dh%27%28x%29%28%5Cdfrac%7Bx%7D%7Bf%28x%29%7D%29%5En)


取 ![math](https://www.zhihu.com/equation?tex=h%28x%29%3Dx) （即普通形式）


![math](https://www.zhihu.com/equation?tex=%5Bx%5En%5Dg%28x%29%3D%5Cdfrac%201n%5Bx%5E%7Bn-1%7D%5D%28%5Cdfrac%7Bx%7D%7Bf%28x%29%7D%29%5En)




例：大朋友与二叉树

求 ![math](https://www.zhihu.com/equation?tex=%5Bx%5En%5Df%28x%29) ，有：


![math](https://www.zhihu.com/equation?tex=f%28x%29%3Dx%2B%5Csum_%7Bi%5Cin%20S%7Df%5Ei%28x%29)


有


![math](https://www.zhihu.com/equation?tex=g%28f%28x%29%29%3Dx%5C%5C%0Ag%28x%29%3D%5Csum_%7Bi%5Cin%20S%7Dx%5Ei-1)


带入求解即可



例：卡特兰数 ![math](https://www.zhihu.com/equation?tex=k) 次幂

求 ![math](https://www.zhihu.com/equation?tex=%5Bx%5E%7Bn-k%7D%5D%28%5Cdfrac%7B1-%5Csqrt%7B1-4x%7D%7D%7B2x%7D%29%5Ek) 

先系数乘以 ![math](https://www.zhihu.com/equation?tex=x%5Ek) ，变为 ![math](https://www.zhihu.com/equation?tex=%5Bx%5En%5D%28%5Cdfrac%7B1-%5Csqrt%7B1-4x%7D%7D%7B2%7D%29%5Ek) 

然后记 ![math](https://www.zhihu.com/equation?tex=g%28x%29%3D%5Cdfrac%7B1-%5Csqrt%7B1-4x%7D%7D%7B2%7D%2Ch%28x%29%3Dx%5Ek) 

那么只要求出 ![math](https://www.zhihu.com/equation?tex=g%28x%29) 的复合逆 ![math](https://www.zhihu.com/equation?tex=f%28x%29) ，直接就有：


![math](https://www.zhihu.com/equation?tex=%5Bx%5E%7Bn-k%7D%5D%28%5Cdfrac%7B1-%5Csqrt%7B1-4x%7D%7D%7B2%7D%29%5Ek%3D%5Bx%5En%5Dh%28g%28x%29%29%3D%5Cdfrac%201n%5Bx%5E%7Bn-1%7D%5Dh%27%28x%29%28%5Cdfrac%7Bx%7D%7Bf%28x%29%7D%29%5En%3D%5Bx%5E%7Bn-k%7D%5D%5Cdfrac%20kn%28%5Cdfrac%7Bx%7D%7Bf%28x%29%7D%29%5En)



解


![math](https://www.zhihu.com/equation?tex=%5Cdfrac%7B1-%5Csqrt%7B1-4f%28x%29%7D%7D2%3Dx)


得


![math](https://www.zhihu.com/equation?tex=f%28x%29%3Dx-x%5E2)


然后可以 ![math](https://www.zhihu.com/equation?tex=O%281%29) 用组合数解了。