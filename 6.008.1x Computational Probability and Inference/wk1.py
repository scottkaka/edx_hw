# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:37:49 2016

@author: sliu
"""

import comp_prob_inference

comp_prob_inference.flip_fair_coin()

dic = {}

dic[2] = 1/36
dic[3] = 2/36
dic[4] = 3/36
dic[5] = 4/36
dic[6] = 5/36
dic[7] = 6/36
dic[8] = 5/36
dic[9] = 4/36
dic[10] = 3/36
dic[11] = 2/36
dic[12] = 1/36


print (dic)
print (dic.values())

sum = 0
for i in dic.values():
    sum += i
    
print(sum)
