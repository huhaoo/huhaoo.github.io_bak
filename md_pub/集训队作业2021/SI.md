先来思考一个更简单的问题：满足至少一半的 ![math](https://www.zhihu.com/equation?tex=p_%7Ba_i%7D%3Cp_%7Bb_i%7D) 。

可以按照 ![math](https://www.zhihu.com/equation?tex=i) 在 ![math](https://www.zhihu.com/equation?tex=a) 中次数减去 ![math](https://www.zhihu.com/equation?tex=b) 中次数排序 ![math](https://www.zhihu.com/equation?tex=v_i) （即一个二元组贡献 ![math](https://www.zhihu.com/equation?tex=%281%2C-1%29) ）。

显然， ![math](https://www.zhihu.com/equation?tex=%5Csum%20v_i%3D0) ，所以每次选出的 ![math](https://www.zhihu.com/equation?tex=v_i%5Cge%200) ，这代表着满足的与不满足的差。

考虑同样地贪心：给初始贡献 ![math](https://www.zhihu.com/equation?tex=%281%2C-2%2C1%29) ，选一次后 ![math](https://www.zhihu.com/equation?tex=%28%2A%2C2%2C-2%29) 。

发现可以通过此题，~~但是是假的~~。
