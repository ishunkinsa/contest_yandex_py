"""Даны две строки, состоящие из строчных латинских букв. 
Требуется определить, являются ли эти строки анаграммами, т. е.
отличаются ли они только порядком следования символов."""

import sys
from collections import defaultdict

def dictFromString(s):
    d =defaultdict(int)
    for c in s:
        d[c] += 1
    return d
def Anogram_check(a, b):
    return dictFromString(a) == dictFromString(b)


s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

if Anogram_check(s1,s2):
    print(1)
else:
    print (0)
