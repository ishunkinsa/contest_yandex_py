"""Даны две строки, состоящие из строчных латинских букв. 
Требуется определить, являются ли эти строки анаграммами, т. е.
отличаются ли они только порядком следования символов."""

def Anogram_check(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    return False

s1 = input()
s2 = input()
if Anogram_check(s1,s2):
    print(1)
else:
    print (0)
