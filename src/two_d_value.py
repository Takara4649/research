import random
import math

def two_d_random_walk_value(n: int, p: float, q: float,r: float,s: float, values_x: list, values_y: list) -> float:
    """
    2次元ランダムウォークの最終値を求める
    Args: n...試行回数, p, q,r,s...確率, values_x,y...実現値
    """
    # 確率のリストを作る
    weights_x = [p, q]
    weights_y = [r, s]
    # ランダムウォークの初期値
    result_x = 0
    result_y = 0
    for i in range(n):
        if i < 3:
            continue
        else:
            result_x += random.choices(values_x,weights=weights_x,k=1)[0]
            result_y += random.choices(values_y,weights=weights_y,k=1)[0]

    return math.sqrt(result_x**2 +result_y**2)
