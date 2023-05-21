"""
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. 
Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память, т.е.,
использует лишь константный объем памяти в процессе работы.
"""

import sys

count = sys.stdin.readline().strip()

ch = -1
m = []
for i in range(int(count)):
    element = sys.stdin.readline().strip()
    if element != ch:
        m.append(element)
    ch = element

for c in m:
    print(c)
