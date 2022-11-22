import random
import itertools
def lx(n:int, p:float, q:float,values_x: list)-> list[float]:
    """２次元ランダムウォークのx座標

    Args:
        n (int): ステップ数
        p (float): 確率
        q (float): 確率
        values_x (list): xの取る値

    Returns:
        list[float]: x座標
    """
    w_x = [p, q]
    lsx = random.choices(values_x, weights=w_x, k=n)
    #lsx = lsx[3:]
    result_x=[result   for result, i in zip(itertools.accumulate(lsx), range(0,n))]
    return result_x
def ly(n:int, r:float, s:float,values_y: list)-> list[float]:
    """２次元ランダムウォークのy座標

    Args:
        n (int): ステップ数
        r (float): 確率
        s (float): 確率
        values_y (list): yの取る値

    Returns:
        list[float]: y座標
    """
    w_y = [r, s]
    lsy = random.choices(values_y, weights=w_y, k=n)
    #lsy = lsy[3:]
    result_y=[result   for result, i in zip(itertools.accumulate(lsy), range(0,n))]
    return result_y
