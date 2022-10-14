# √2npqlog(log(n)) - |S_n - np| > 0 になる確率が1に近づくことを確認する
# 必要なモジュールをインポートする
import matplotlib.pyplot as plt

import math

from src.limsup import *
from src.simple_random_walk import *


#  パラメータを設定する
## 試行回数
n = 1000
## サンプルパスの本数
m = 50
p = 1/2
q = 1 - p
values = [1, 0]

# 上極限の点をプロットする
xs = [i for i in range(3, n)]
xs.insert(0, math.e)
ys_upper = [limsup(i, p, q) for i in range(3, n)]
ys_upper.insert(0, limsup(math.e, p, q))
plt.plot(xs, ys_upper, label="ls", color="blue")
ys_lower = [-limsup(i, p, q) for i in range(3, n)]
ys_lower.insert(0, limsup(math.e, p, q))
plt.plot(xs, ys_lower, label="ls", color="blue")

# 1次元ランダムウォークの点をm回プロットする
for _ in range(m):
    zs = [i for i in range(3, n)]
    zs.insert(0, 0)
    ws = simple_random_walk(n, p, q, values)
    ws.insert(0, 0)
    plt.plot(zs, ws, label="s_walk", color="red")

# グラフを描画する
plt.title("limsup_with_simple_random_walk")
plt.xticks(range(0, n+1, n//10))
print("done :)")
plt.savefig("img/limsup_with_simple_random_walk.png")
plt.show()
