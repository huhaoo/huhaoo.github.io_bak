### Plants

记 ![math](https://www.zhihu.com/equation?tex=R_u) 表示植物 ![math](https://www.zhihu.com/equation?tex=u) 能比对到的植物集合。

首先如果有 ![math](https://www.zhihu.com/equation?tex=r_i%3D0) ，且不存在 ![math](https://www.zhihu.com/equation?tex=r_j%3D0%2Ci%5Cin%20R_j) ，那么。

1. 不存在 ![math](https://www.zhihu.com/equation?tex=k) 使得 ![math](https://www.zhihu.com/equation?tex=k) 一定比 ![math](https://www.zhihu.com/equation?tex=i) 高。
2. 对于所有满足 ![math](https://www.zhihu.com/equation?tex=j%5Cin%20R_i%5Cor%20i%5Cin%20R_j) 的 ![math](https://www.zhihu.com/equation?tex=j) ，一定有 ![math](https://www.zhihu.com/equation?tex=h_i%3Eh_j) 。

 ![math](https://www.zhihu.com/equation?tex=2) 很好证： ![math](https://www.zhihu.com/equation?tex=j%5Cin%20R_i) 部分由定义可得，然后剩下的部分由一个显然的结论“若 ![math](https://www.zhihu.com/equation?tex=r_u%5Cnot%3D0%2C%5Cforall%20w%5Cin%20R_u%2Ch_v%5Cge%20h_w) ，则 ![math](https://www.zhihu.com/equation?tex=h_v%3Eh_u) ”可得。

 ![math](https://www.zhihu.com/equation?tex=1) 的话由于不存在与 ![math](https://www.zhihu.com/equation?tex=i) 有关的限制高度大于 ![math](https://www.zhihu.com/equation?tex=i) ，所以 ![math](https://www.zhihu.com/equation?tex=1) 也是成立的。

所以可以这样：

1. 每次找一个 ![math](https://www.zhihu.com/equation?tex=i) ，使得 ![math](https://www.zhihu.com/equation?tex=r_i%3D0) ，且不存在 ![math](https://www.zhihu.com/equation?tex=r_j%3D0%2Ci%5Cin%20R_j) 。
2. 对于所有满足 ![math](https://www.zhihu.com/equation?tex=j%5Cin%20R_i%5Cor%20i%5Cin%20R_j) 的 ![math](https://www.zhihu.com/equation?tex=j) ，连一条 ![math](https://www.zhihu.com/equation?tex=i%5Crightarrow%20j) 的边。
3. 删除 ![math](https://www.zhihu.com/equation?tex=i) ，可以由此使 ![math](https://www.zhihu.com/equation?tex=i%5Cin%20R_j) 的 ![math](https://www.zhihu.com/equation?tex=j) 的 ![math](https://www.zhihu.com/equation?tex=r_j) 减一，且删去 ![math](https://www.zhihu.com/equation?tex=R_j) 中的 ![math](https://www.zhihu.com/equation?tex=i) 。
4. 询问 ![math](https://www.zhihu.com/equation?tex=u) 是否高于 ![math](https://www.zhihu.com/equation?tex=v) 时，只需判断是否找得到一条 ![math](https://www.zhihu.com/equation?tex=u) 到 ![math](https://www.zhihu.com/equation?tex=v) 的路径。

不妨记下每个点被删除的时间 ![math](https://www.zhihu.com/equation?tex=t_u) ，然后对于最初的 ![math](https://www.zhihu.com/equation?tex=R) 考虑。

存在 ![math](https://www.zhihu.com/equation?tex=u%5Crightarrow%20v) ，当且仅当 ![math](https://www.zhihu.com/equation?tex=t_u%3Ct_v%2Cu%5Cin%20R_v%5Cor%20v%5Cin%20R_u) 。

由于 ![math](https://www.zhihu.com/equation?tex=t) 的值可以方便地 ![math](https://www.zhihu.com/equation?tex=O%28n%5Clog%20n%29) 求解，所以只需考虑一个传递闭包问题。

因为：

* 若 ![math](https://www.zhihu.com/equation?tex=v%2Cw%5Cin%20R_u%2Ct_w%3Et_v%3Et_u) ，则一定存在 ![math](https://www.zhihu.com/equation?tex=v%5Crightarrow%20w) ， ![math](https://www.zhihu.com/equation?tex=u%5Cin%20R_v%2Cu%5Cin%20R_w) 同理。

  这样可以只对 ![math](https://www.zhihu.com/equation?tex=v%5Cin%20R_u%2Ct_v%3Et_u) 和 ![math](https://www.zhihu.com/equation?tex=u%5Cin%20R_w%2Ct_w%3Et_u) 中 ![math](https://www.zhihu.com/equation?tex=t) 最小的 ![math](https://www.zhihu.com/equation?tex=v%2Cw) 连边即可。

这样可以只连一共 ![math](https://www.zhihu.com/equation?tex=2n) 条边，复杂度 ![math](https://www.zhihu.com/equation?tex=O%28%5Cdfrac%7Bn%5E2%7D%5Comega%29) ，~~如果空间给8G是可以通过此题的~~。

考虑到连边的特殊性，若存在一条路径，则一定存在一条只向左/向右的路径，因为入边一共只可能有两条（易证），且一左一右，所以可以倍增求解。

复杂度 ![math](https://www.zhihu.com/equation?tex=O%28n%5Clog%20n%29) 。

### Supertrees

若有 ![math](https://www.zhihu.com/equation?tex=3) ，一定不行。

若只有 ![math](https://www.zhihu.com/equation?tex=1) ，则一定是由很多链组成。

找到每个联通块，找到每条链，然后有 ![math](https://www.zhihu.com/equation?tex=2) 的时候连个环即可。

复杂度 ![math](https://www.zhihu.com/equation?tex=O%28n%5E2%29) 。

### Tickets

贪心，每一次相当于找 ![math](https://www.zhihu.com/equation?tex=%5Cdfrac%20n2) 个正贡献的和 ![math](https://www.zhihu.com/equation?tex=%5Cdfrac%20n2) 负贡献的。

先找 ![math](https://www.zhihu.com/equation?tex=nk) 个正贡献的，然后贪心地删去 ![math](https://www.zhihu.com/equation?tex=%5Cdfrac%7Bnk%7D%7B2%7D) 个成正贡献加入 ![math](https://www.zhihu.com/equation?tex=%5Cdfrac%7Bnk%7D%7B2%7D) 个负贡献即可，注意需要满足每一种颜色总共有 ![math](https://www.zhihu.com/equation?tex=k) 个。

复杂度 ![math](https://www.zhihu.com/equation?tex=O%28n%5E2%5Clog%20n%29) 。