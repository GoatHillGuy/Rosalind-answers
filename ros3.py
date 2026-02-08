#!/usr/bin/env python3

def odd (a, b):
    oddlist = []
    for i in range(a, b+1):
        if i%2 != 0:
            oddlist.append(i)
        else:
            pass

    print(sum(oddlist))

odd(4712, 9041)

