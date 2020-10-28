可以先写一个 ![math](https://www.zhihu.com/equation?tex=O%28%5Cmathrm%7Bpoly%7D%28n%292%5E%7B2n%7D%29) 的搜索，可以得到：

1. 先将`aa,bb`凑在一起，然后再依次归位。
2. 过程中会经常出现类似`aabb`的字串，提示我们可以按模 ![math](https://www.zhihu.com/equation?tex=4) 的取值分类讨论。

打出 ![math](https://www.zhihu.com/equation?tex=n) 比较小的表，容易得到构造方法。

实现时按结论 ![math](https://www.zhihu.com/equation?tex=1) 分两步操作即可。

具体的，在某一步时，可以先写出结束后的字符串，然后比较这两个字符串的不同，然后依次将不同的地方修复。
