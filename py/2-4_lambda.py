# -*- coding: utf-8 -*-

# ラムダ

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = filter(lambda x: x % 2, nums)
print("odds", odds)

f = (lambda x: x)
print("f", f)

odds_sq = map(lambda x: x * x, odds)
print("odds_sq", odds_sq)

reduced = reduce(lambda x, y: x + y, odds_sq)
print("reduced", reduced)


