~~理解题意比做法难道不知道哪去了。~~

如果有三个串长度相同就无解。

考虑记 ![math](https://www.zhihu.com/equation?tex=f%28a%2Cb%29) 为 ![math](https://www.zhihu.com/equation?tex=a) 能否变为 ![math](https://www.zhihu.com/equation?tex=b) 。

记 ![math](https://www.zhihu.com/equation?tex=x%2Cy) 为两个操作序列最后一位。

按长度顺序加入 ![math](https://www.zhihu.com/equation?tex=z) ，则：

1. 若 ![math](https://www.zhihu.com/equation?tex=f%28x%2Cz%29%3Df%28y%2Cz%29%3D0) ，则无解。
2. 若 ![math](https://www.zhihu.com/equation?tex=f%28x%2Cz%29%3Df%28y%2Cz%29%3D1) ，则可以找到一个序列 ![math](https://www.zhihu.com/equation?tex=z_%7B1%5Cdots%20m%7D%2Cz_1%3Dz) ，且 ![math](https://www.zhihu.com/equation?tex=f%28z_%7Bi%7D%2Cz_%7Bi%2B1%7D%29%3D1%2Cf%28z_%7Bm-1%7D%2Cz_m%29%3D0) ，若 ![math](https://www.zhihu.com/equation?tex=f%28x%2Cz_m%29%3D1) ，则令 ![math](https://www.zhihu.com/equation?tex=x%3Dz_m%2Cy%3Dz_%7Bm-1%7D) ，反之亦然。
3. 否则，若 ![math](https://www.zhihu.com/equation?tex=f%28x%2Cz%29%3D0) ，令 ![math](https://www.zhihu.com/equation?tex=x%3Dz) ，否则令 ![math](https://www.zhihu.com/equation?tex=y%3Dz) 。
