# -*- coding: utf-8 -*-
from collections import Counter, defaultdict, OrderedDict

# collection
items = ["F", "C", "C", "A", "B", "A", "C", "E", "F"]
cntr = Counter(items)
print(cntr)
cntr["C"] -= 1
print(cntr)

# defaultdict
d = defaultdict(int)

for item in items:
    d[item] += 1

print(d)

print(OrderedDict(sorted(d.items(), key=lambda i: i[1])))


