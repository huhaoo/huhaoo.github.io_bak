任意基DFT即求：

> 

![math](https://render.githubusercontent.com/render/math?math=%3E%20%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Da_ix%5Ei%28bp%5Ei%2Bc%29%5Ej%0A%3E)



先说一个简易版（循环卷积）：

> 

![math](https://render.githubusercontent.com/render/math?math=%3E%20%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Da_jp%5E%7Bij%7Dx%5Ei%0A%3E)



直接分离 ![math](https://render.githubusercontent.com/render/math?math=ij) 即可（ ![math](https://render.githubusercontent.com/render/math?math=ij%3D%7Bi%2Bj%5Cchoose%202%7D-%7Bi%5Cchoose%202%7D-%7Bj%5Cchoose%202%7D) ）：


![math](https://render.githubusercontent.com/render/math?math=%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Da_jp%5E%7B%7Bi%2Bj%5Cchoose%202%7D-%7Bi%5Cchoose%202%7D-%7Bj%5Cchoose%202%7D%7Dx%5Ei%3D%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7Dx%5Eip%5E%7B-%7Bi%5Cchoose%202%7D%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Dp%5E%7B%7Bi%2Bj%5Cchoose%202%7D-%7Bj%5Cchoose%202%7D%7Da_j)


后面那个直接NTT就行了。

然后是任意基DFT：


![math](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0A%26%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Da_jx%5Ei%28bp%5Ei%2Bc%29%5Ej%5C%5C%0A%3D%26%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7D%5Csum_%7Bk%7Da_jx%5Ei%28bp%5Ei%29%5Ekc%5E%7Bj-k%7D%7Bj%5Cchoose%20k%7D%5C%5C%0A%3D%26%5Csum_%7Bi%3D0%7D%5E%7Bn-1%7Dx%5Ei%5Csum_%7Bk%3D0%7D%5E%7Bm-1%7D%28bp%5Ei%29%5Ekc%5E%7B-k%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Da_jc%5E%7Bj%7D%7Bj%5Cchoose%20k%7D%5C%5C%0A%5Cend%7Balign%7D)


直接卷出


![math](https://render.githubusercontent.com/render/math?math=%5Chat%20a_k%3Db%5Ekc%5E%7B-k%7D%5Csum_%7Bj%3D0%7D%5E%7Bm-1%7Da_jc%5Ej%7Bj%5Cchoose%20k%7D)


然后就是上面的子问题了



