import math


# 上極限を求める
def limsup(n: int, p: float, q: float) -> float:
    """
    上極限を求める
    Args: n...試行回数, p, q...確率
    """
    return math.sqrt(2 * n * p * q * math.log(math.log(n)))
