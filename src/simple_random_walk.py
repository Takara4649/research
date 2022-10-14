import random
import itertools


# 1次元ランダムウォークを求める
def simple_random_walk(n: int, p: float, q: float, values: list) -> float:
    """
    1次元ランダムウォークを求める
    Args: n...試行回数, p, q...確率, values...実現値
    """
    # 確率のリストを作る
    weights = [p, q]
    # サンプルパスを作る
    paths = random.choices(values, weights=weights, k=n)
    # 添え字i = 0, 1, 2の値を削除する
    for _ in range(3):
        paths.pop(0)
    results = [result - i*p for result, i in zip(itertools.accumulate(paths), range(3,n))]
    return results
