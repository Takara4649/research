import random
import itertools
import math



# 1次元ランダムウォークを求める
def simple_random_walk_divided2(n: int, p: float, q: float, values: list) -> list[float]:
    """
    1次元ランダムウォークを求める
    Args: n...試行回数, p, q...確率, values...実現値
    """
    # 確率のリストを作る
    weights = [p, q]
    # サンプルパスを作る
    paths = random.choices(values, weights=weights, k=n)
    # 添え字i = 0, 1, 2の値を削除する
    paths = paths[3:]
    results = [(result-i*p) / math.sqrt(i*math.log(i)) for result, i in zip(itertools.accumulate(paths), range(3,n))]
    return results
