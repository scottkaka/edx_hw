# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = 'abcdefghijklmnopqrstuvwxyz'
alpha = 'abcdefghijklmnopqrstuvwxyz'
substring = ''
pos = 0
l = 0
longest = ''
for i in s:
    if alpha.find(i) >= pos:
        substring = substring + i
        pos = alpha.find(i)
    elif len(substring) > l :
        longest = substring
        l = len(longest)
        substring = i
        pos = alpha.find(i)
    else:
        substring = i
        pos = alpha.find(i)
if len(substring)>len(longest):
    longest = substring
        
print ('Longest substring in alphabetical order is: '+ longest)