# 1次元ランダムウォークの最終値の絶対値が上極限を越える回数を求める
# 必要なモジュールをインポートする
import matplotlib.pyplot as plt

from src.limsup import limsup
from src.simple_random_walk_value import simple_random_walk_value


#  パラメータを設定する
## 試行回数
a = 7
ns = [pow(10, i) for i in range(1, a)]
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
        srw = simple_random_walk_value(n, p, q, values)
        if abs(srw) >= limsup(n, p, q):
            cnt += 1
    cnts.append(cnt)

# グラフを描画する
plt.title(f"count_outside_paths (k = {a-1})")
plt.xticks(range(1, a))
plt.plot(range(1, a), cnts, color="blue")
plt.savefig(f"img/count_outside_paths_{a}.png")
plt.grid()
plt.show()
