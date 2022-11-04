import random


def simple_random_walk_value(n: int, p: float, q: float, values: list) -> float:
    """
    1次元ランダムウォークの最終値を求める
    Args: n...試行回数, p, q...確率, values...実現値
    """
    # 確率のリストを作る
    weights = [p, q]
    # ランダムウォークの初期値
    result = 0
    for i in range(n):
        if i < 3:
            continue
        else:
            result += random.choices(values,weights=weights,k=1)[0]
    return result - n*p
