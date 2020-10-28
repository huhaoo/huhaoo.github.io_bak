可以记一个变量的状态为 ![math](https://render.githubusercontent.com/render/math?math=s_i%3D4v_i%5E1%2B2v_i%5E2%2B1v_i%5E3) 。

若 ![math](https://render.githubusercontent.com/render/math?math=s_i%3Ds_j) ，它们由已知条件可以推得它们恒等，可以用 ![math](https://render.githubusercontent.com/render/math?math=x_i%5Crightarrow%20x_j%2Cx_j%5Crightarrow%20x_i) 来代替与之等价的条件。

若 ![math](https://render.githubusercontent.com/render/math?math=s_i%3D0) 或 ![math](https://render.githubusercontent.com/render/math?math=s_i%3D7) ，可以推得它们恒为 ![math](https://render.githubusercontent.com/render/math?math=0/1) ，可以用 ![math](https://render.githubusercontent.com/render/math?math=x_i%5Crightarrow%20%21x_i/%21x_i%5Crightarrow%20x_i) 来代替。

若 ![math](https://render.githubusercontent.com/render/math?math=s_i%2Bs_j%3D7) ，可以推得它们恒不等，可以用 ![math](https://render.githubusercontent.com/render/math?math=x_i%5Crightarrow%20%21x_j%2C%21x_i%5Crightarrow%20x_j) 来代替。

那么可以简化为 ![math](https://render.githubusercontent.com/render/math?math=n%5Cle%203) 的问题：一共有最多 ![math](https://render.githubusercontent.com/render/math?math=2%5E%7B12%7D) 种可能的约束方案，可以暴力搜索它们是否可行，最粗暴的实现可以 ![math](https://render.githubusercontent.com/render/math?math=O%282%5E%7B12%7D2%5E3%29) 求解。
