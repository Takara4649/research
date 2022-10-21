# √2npqlog(log(n)) - |S_n - np| > 0 になる確率が1に近づくことを確認する
# 必要なモジュールをインポートする
import matplotlib.pyplot as plt

import math

from src.limsup import limsup
from src.simple_random_walk import simple_random_walk


#  パラメータを設定する
## 試行回数
k = 10
ns = [pow(4, i) for i in range(1, k)]
## サンプルパスの本数
m = 100
p = 1/2
q = 1 - p
values = [1, 0]
#パスが飛び出た本数を記録
cnts = []

# 1次元ランダムウォークの点をm回プロットする
for n in ns:
    cnt = 0
    for _ in range(m):
        srw = simple_random_walk(n, p, q, values)
        if srw[-1] >= limsup(n, p, q):
            cnt += 1
    cnts.append(cnt)


# グラフを描画する
plt.title("count_outside_paths")
plt.xticks(range(1, k))
plt.plot(range(1, k), cnts, color="blue")
print("done :)")
plt.savefig("img/count_outside_paths.png")
plt.show()
