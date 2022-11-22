# limsup(|S_n - np|/√2npqlog(log(n))) = 1となる確率が1に近づくことを確認する
# 必要なモジュールをインポートする
import matplotlib.pyplot as plt
import numpy as np

import math

from src.limsup import limsup
from src.simple_random_walk_divided import simple_random_walk_divided


#  パラメータを設定する
## 試行回数
n = 100000
## サンプルパスの本数
m = 100
p = 1/2
q = 1 - p
values = [1, 0]

# y=|1|の直線をプロットする
xs = [i for i in range(n)]
ys_upper = [1] * n
plt.plot(xs, ys_upper, label="ls", color="blue")
ys_lower = [-1] * n
plt.plot(xs, ys_lower, label="ls", color="blue")


# 1次元ランダムウォークの点をm回プロットする
for _ in range(m):
    zs = [i for i in range(3, n)]
    zs.insert(0, 0)
    ws = simple_random_walk_divided(n, p, q, values)
    ws.insert(0, 0)
    plt.plot(zs, ws, label="s_walk", color="red",lw=0.01)

# グラフを描画する
plt.title("simple_random_walk_divided")
plt.xticks(range(0, n+1, n//10))
print("done :)")
plt.savefig("img/simple_random_walk_divided.png")
plt.show()
