# -*- coding: utf-8 -*-

def get_counter(inc):
    # count = 0
    vars = {"count": 0}
    def add():
        # UnboundLocalError: 変更可能な変数のスコープは基本ローカルのみ。(読みだしは可能)
        # count += inc
        # print('current: ' + str(count))

        # dictの中身は変更可能
        vars["count"] += inc
        print('current count: ' + str(vars['count']))
    return add


cntr = get_counter(2)
cntr()
cntr()

cntr = get_counter(3)
cntr()
