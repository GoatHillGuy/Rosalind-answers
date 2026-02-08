#!/usr/bin/env python3

f = open('example.txt', 'r')
for i, line in enumerate(f):
    if (i+1)%2 == 0:
        print(line)

