不妨用 ![math](https://render.githubusercontent.com/render/math?math=%5Cepsilon) 来代替题目中的 ![math](https://render.githubusercontent.com/render/math?math=t) ，因为一般 ![math](https://render.githubusercontent.com/render/math?math=t) 出现时表示时间。

考虑敲击的含义，在时刻 ![math](https://render.githubusercontent.com/render/math?math=t) 敲击位置 ![math](https://render.githubusercontent.com/render/math?math=p) ，可以判断 ![math](https://render.githubusercontent.com/render/math?math=v) 和 ![math](https://render.githubusercontent.com/render/math?math=%5Cdfrac%20pt) 的大小关系，可以发现，条件允许时，尽可能早地敲击一定时最优的。

一个直观的想法，若确定了Flubber的流速在 ![math](https://render.githubusercontent.com/render/math?math=%5Bv%2Cv%2B%5Cepsilon%5D) 中，可以推测流速为 ![math](https://render.githubusercontent.com/render/math?math=v%2B%5Cdfrac%20%5Cepsilon2) ，就一定满足题意。

若要确定流速在 ![math](https://render.githubusercontent.com/render/math?math=%5Bv-v_0%2Cv%5D%2Cv_0%3C%5Cepsilon) 间，则不如放大范围，确定它在 ![math](https://render.githubusercontent.com/render/math?math=%5Bv-%5Cepsilon%2Cv%5D) 间，因为后者更好解决，且都满足题意。

这启示我们可以将 ![math](https://render.githubusercontent.com/render/math?math=%5Bv_1%2Cv_2%5D) 分为若干段，每段长为 ![math](https://render.githubusercontent.com/render/math?math=%5Cepsilon) ，类似二分地敲击分界点。

若长度非 ![math](https://render.githubusercontent.com/render/math?math=%5Cepsilon) 的整倍数，容易发现，第 ![math](https://render.githubusercontent.com/render/math?math=1) 段（以 ![math](https://render.githubusercontent.com/render/math?math=v_1) 为左端点的段）不满长度 ![math](https://render.githubusercontent.com/render/math?math=%5Cepsilon) （而其它段长度都为 ![math](https://render.githubusercontent.com/render/math?math=%5Cepsilon) ）是较优的。

接下来问题转化为了：直线上有若干个点 ![math](https://render.githubusercontent.com/render/math?math=1%5Cdots%20m) ，你需要建出一颗分治树，每个点都有限制——它的深度不大于一个值 ![math](https://render.githubusercontent.com/render/math?math=D_i) ，使得这棵树的深度最小。

若要判断答案 ![math](https://render.githubusercontent.com/render/math?math=%5Crm%20ans) 是否可行，我们可以将所有 ![math](https://render.githubusercontent.com/render/math?math=D) 对 ![math](https://render.githubusercontent.com/render/math?math=%5Crm%20ans) 取 ![math](https://render.githubusercontent.com/render/math?math=%5Cmin) ，然后判断是否可行。  
所以可以先想怎么判断可行性。

考虑一颗深度为 ![math](https://render.githubusercontent.com/render/math?math=10%5E%7B100%7D) 的满二叉树，可以任意地填入 ![math](https://render.githubusercontent.com/render/math?math=1%5Cdots%20m) ，满足每个点最多出现一个数，它们在中序遍历依次出现（ ![math](https://render.githubusercontent.com/render/math?math=dfn) 依次增大），且第 ![math](https://render.githubusercontent.com/render/math?math=i) 个点的深度不大于 ![math](https://render.githubusercontent.com/render/math?math=D_i) 。

可以贪心地填：从 ![math](https://render.githubusercontent.com/render/math?math=m) 到 ![math](https://render.githubusercontent.com/render/math?math=1) （因为标号越大， ![math](https://render.githubusercontent.com/render/math?math=D) 越不容易被改变）依次填，每次填入 ![math](https://render.githubusercontent.com/render/math?math=dfn) 最大但小于上一次的深度不大于 ![math](https://render.githubusercontent.com/render/math?math=D_i) 的位置。

因为一颗子树能填入的 ![math](https://render.githubusercontent.com/render/math?math=D_i%5Cle%20k) 的数的个数很容易求。  
所以可以从后往前填，每次求当前状态能满足的最小答案，然后如果它是一个可行的答案，那么它一定不大于剩下的最小的 ![math](https://render.githubusercontent.com/render/math?math=D) 的值。

统计最小的可行的答案即可。

因为 ![math](https://render.githubusercontent.com/render/math?math=D) 相同的可以一起处理，而 ![math](https://render.githubusercontent.com/render/math?math=D) 只有 ![math](https://render.githubusercontent.com/render/math?math=%5Csqrt%20l) 种取值，所以复杂度根据实现为 ![math](https://render.githubusercontent.com/render/math?math=O%28c%28%5Clog%20l%2B%5Csqrt%20l%29%29%5Csim%20O%28c%5Clog%20l%5Csqrt%20l%29) 。
