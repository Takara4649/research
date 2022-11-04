from matplotlib import patches
import math


# 上極限を求める
def inside_circle(n: int, eps: float):
    """内側の円を描く

    Args:
        n (int): ステップ数
        eps (float): 微小誤差

    Returns: 内側の円
    """

    return patches.Circle((0,0), math.sqrt((2-eps)*n*math.log(math.log(n))), edgecolor="red", lw=0.1)


def outside_circle(n: int, eps: float):
    """外側の円

    Args:
        n (int): ステップ数
        eps (float): 微小誤差

    Returns: 外側の円
    """

    return patches.Circle((0,0), math.sqrt((2+eps)*n*math.log(math.log(n))), edgecolor="red",lw=0.1)
