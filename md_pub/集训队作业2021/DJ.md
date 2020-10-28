转化Flubber和水一样的代价，但价值为 ![math](https://render.githubusercontent.com/render/math?math=%28%5Cdfrac%20Fv%29%5EaW%5E%7B1-a%7D%3D%5Cdfrac%201%7Bv%5Ea%7DF%5EaW%5E%7B1-a%7D) 。

考虑到，若新建 ![math](https://render.githubusercontent.com/render/math?math=0%5Crightarrow%201%2C2) ，那么原来以 ![math](https://render.githubusercontent.com/render/math?math=1%2C2) 为源点的流量和以为源点 ![math](https://render.githubusercontent.com/render/math?math=0) 的流量相同。

因为价值为增函数，所以一定是一个最大流。

若最大流为 ![math](https://render.githubusercontent.com/render/math?math=f_0) ，Flubber流量为 ![math](https://render.githubusercontent.com/render/math?math=f_1) ，水流量为 ![math](https://render.githubusercontent.com/render/math?math=f_2) ，则 ![math](https://render.githubusercontent.com/render/math?math=f_2%3Df_0-f_1) ，可以先求出 ![math](https://render.githubusercontent.com/render/math?math=f_1%5Cin%5Bl%2Cr%5D) ，转化为求：



![math](https://render.githubusercontent.com/render/math?math=%5Cmax%20f%28x%29%3Dx%5Ea%28f_0-x%29%5E%7B1-a%7D%2Cx%5Cin%5Bl%2Cr%5D)



因为



![math](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0Af%27%28x%29%3D%26x%5Ea%28f_0-x%29%5E%7B1-a%7D%28%5Cdfrac%7Ba%7D%7Bx%7D-%5Cdfrac%7B%281-a%29%7D%7Bf_%7B0%7D-x%7D%29%5C%5C%0A%3D%26x%5E%7Ba-1%7D%28f_0-x%29%5E%7B-a%7D%28af_0-x%29%5C%5C%0Af%27%27%28x%29%3D%26%28af_0-x%29x%5E%7Ba-1%7D%28f_0-x%29%5E%7B-a%7D%28-%5Cdfrac%7B1%7D%7Baf_0-x%7D%2B%5Cdfrac%7B%28a-1%29%7Dx-%5Cdfrac%7B-a%7D%7Bf_0-x%7D%29%5C%5C%0A%3D%26%28a-1%29af_0%5E2%28f_0-x%29%5E%7B-1-a%7Dx%5E%7Ba-2%7D%3C0%0A%5Cend%7Balign%7D)



所以 ![math](https://render.githubusercontent.com/render/math?math=f%28x%29) 是凸函数，三分即可。
