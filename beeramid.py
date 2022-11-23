def beeramid(bonus, price):
    cans = int(bonus/price)
    level = 0
    while ((level+1)**2 <= cans):
        level += 1
        cans -= level*level
    return level