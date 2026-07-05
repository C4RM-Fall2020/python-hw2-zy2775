import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy

    t = np.arange(1, n + 1)
    coupon = face * couponRate / ppy

    cash_flows = np.full(n, coupon, dtype=float)
    cash_flows[-1] += face

    pv_cash_flows = cash_flows / (1 + r) ** t
    price = np.sum(pv_cash_flows)

    duration = np.sum((t / ppy) * pv_cash_flows) / price
    return duration
