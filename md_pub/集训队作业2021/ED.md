考虑到，如果确定最终状态，第 ![math](https://render.githubusercontent.com/render/math?math=i) 个人有 ![math](https://render.githubusercontent.com/render/math?math=a_i) 个宝石，那么它出现的概率为：


![math](https://render.githubusercontent.com/render/math?math=%5Cdfrac%7Bd%21%7D%7B%5Cprod_i%20%28a_i-1%29%21%7D%5Cdfrac%7B%5Cprod_i%20%28a_i-1%29%21%7D%7Bn%5E%7B%5Coverline%20d%7D%7D%3D%5Cdfrac%7Bd%21%7D%7Bn%5E%7B%5Coverline%20d%7D%7D)


不难发现，原题相当于：

对于所有 ![math](https://render.githubusercontent.com/render/math?math=%5Csum_ia_i%3Dd) ，求 ![math](https://render.githubusercontent.com/render/math?math=%5Csum_%7Bi%5Cle%20r%7D%28%5Cmax_i%28a%29%2B1%29) 的期望。

~~如果对质数 ![math](https://render.githubusercontent.com/render/math?math=p) 取模很好做。~~

简单DP即可。

~~卡了一天，发现`long double`其实可以处理。~~