# limsup(|S_n - np|/√2npqlog(log(n))) = 1となる確率が1に近づくことを確認する
# 必要なモジュールをインポートする
import matplotlib.pyplot as plt
import numpy as np

import math

from src.limsup import limsup
from src.simple_random_walk_divided2 import simple_random_walk_divided2


#  パラメータを設定する
## 試行回数
n = 10000
## サンプルパスの本数
m = 50
p = 1/2
q = 1 - p
values = [1, 0]



#y=1/sqrt2のグラフをプロット
xs = [i for i in range(n)]
ys_upper = [1/math.sqrt(2)] * n
plt.plot(xs, ys_upper, label="ls", color="green")
ys_lower = [-1/math.sqrt(2)] * n
plt.plot(xs, ys_lower, label="ls", color="green")


# 1次元ランダムウォークの点をm回プロットする
for _ in range(m):
    zs = [i for i in range(3, n)]
    zs.insert(0, 0)
    ws = simple_random_walk_divided2(n, p, q, values)
    ws.insert(0, 0)
    plt.plot(zs, ws, label="s_walk", color="red",lw=0.1)

# グラフを描画する
plt.title("simple_random_walk_divided2")
plt.xticks(range(0, n+1, n//10))
print("done :)")
plt.savefig("img/simple_random_walk_divided2.png")
plt.show()
