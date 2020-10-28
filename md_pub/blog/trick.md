`i64*i64%i64`的快速方法：

```cpp
inline i64 mul(i64 a,i64 b,i64 p)
{
	i64 ans=(i64)((unsigned i64)a*b)-(i64)((unsigned i64)((long double)a*b/p+0.5)*p);
	return ans<0?ans+p:ans;
}
```

（`long double`精度~~应该~~够用）

---

两个凸包合并（上凸包），问某点的高度。

预处理时记录最高点（或三分），共划分为4个凸包，只有单调上升/下降的才需要讨论。

二分第一个凸包的位置（差分和递减）。