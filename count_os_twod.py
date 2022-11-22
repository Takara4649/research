# 2次元ランダムウォークの最終値の絶対値が上極限を越える回数を求める
# 必要なモジュールをインポートする
import matplotlib.pyplot as plt
import math
import numpy as np

#from src.circle import outside_circle
from src.two_d_value import two_d_random_walk_value


#  パラメータを設定する
## 試行回数
k = 7
ns = [pow(10, i) for i in range(1, k)]
## サンプルパスの本数
m = 150
p = 0.5
q = 1-p
r = 0.5
s = 1-r
eps = 1
values_x = [1, -1]
values_y = [1, -1]
#パスが飛び出た本数を記録
cnts = []

# 2次元ランダムウォークの点をm回プロットする
for n in ns:
    cnt = 0
    for _ in range(m):
        srw = two_d_random_walk_value(n, p, q, r, s, values_x, values_y)
        if srw >= math.sqrt((2+eps)*n*math.log(math.log(n))):
            cnt += 1
    cnts.append(cnt)

# グラフを描画する
plt.title(f"count_two_d_os_paths (k = {k-1})")
plt.xticks(range(1, k))
plt.yticks(np.arange(0,101,step=1))
plt.plot(range(1, k), cnts, color="blue")
plt.savefig(f"img/count_outside_paths_{k}.png")
plt.grid()
plt.show()
