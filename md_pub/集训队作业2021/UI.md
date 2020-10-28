因为`FRF`和`C`等价，所以可以用`R r`代替`C c`。

我们可以按这个操作顺序来操作：`R r (F) D|D R r (F)`（下记为`A|B`），因为`B`操作可逆（事实上所有都可逆），所以考虑对 ![math](https://www.zhihu.com/equation?tex=i) 做`A`，对 ![math](https://www.zhihu.com/equation?tex=j) 做`B`。  
考虑一个中间状态 ![math](https://www.zhihu.com/equation?tex=P_0) ，使得 ![math](https://www.zhihu.com/equation?tex=P_i) 可以通过`A`到达 ![math](https://www.zhihu.com/equation?tex=P_0) ， ![math](https://www.zhihu.com/equation?tex=P_0) 可以通过`B`到达 ![math](https://www.zhihu.com/equation?tex=P_j) ，由于左右两侧都有`D`，所以不妨令 ![math](https://www.zhihu.com/equation?tex=P_0) 合法当且仅当不能通过`D`操作使字典序变小。  
因为本质不同的`C c`操作只有 ![math](https://www.zhihu.com/equation?tex=6%5E4) 种，所以可以枚举 ![math](https://www.zhihu.com/equation?tex=P_%7Bj%27%7D) ，使它可以到达 ![math](https://www.zhihu.com/equation?tex=P_j) ，又这时有唯一的 ![math](https://www.zhihu.com/equation?tex=P_0) 与 ![math](https://www.zhihu.com/equation?tex=P_j) ，所以可以推得合法的 ![math](https://www.zhihu.com/equation?tex=P_0) 不超过 ![math](https://www.zhihu.com/equation?tex=m%3D2%5Ctimes%206%5E4) 种。  
 ![math](https://www.zhihu.com/equation?tex=P_i) 同理， ![math](https://www.zhihu.com/equation?tex=P_i) 可到的合法的 ![math](https://www.zhihu.com/equation?tex=P_0) 只有 ![math](https://www.zhihu.com/equation?tex=m) 种。

map即可，复杂度 ![math](https://www.zhihu.com/equation?tex=O%28nm%5Clog%28nm%29%29) 
