"""
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
Желательно получить решение, работающее за линейное время и при этом проходящее по входному
массиву только один раз.
"""

import sys

count = sys.stdin.readline().strip()

cnt = 0
max_cnt = 0
for i in range(int(count)):
    element = sys.stdin.readline().strip()
    if element == '1':
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 0

print(max_cnt if max_cnt > cnt else cnt)
