import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy

    t = np.arange(1, n + 1)
    coupon = face * couponRate / ppy

    cash_flows = np.full(n, coupon, dtype=float)
    cash_flows[-1] += face

    price = np.sum(cash_flows / (1 + r) ** t)
    return price
