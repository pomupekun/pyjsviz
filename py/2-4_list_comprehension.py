# -*- coding: utf-8 -*-

# A. リスト内包表記
nums = range(10)
print(nums)

odd_squares = [x * x for x in nums if x % 2]
print(odd_squares)

print(sum(odd_squares))


def is_odd(x):
    return x % 2


def sq(x):
    return x * x


# B. 関数化によるAの可読性向上
sum = sum([sq(x) for x in range(10) if is_odd(x)])
print("sum", sum)


