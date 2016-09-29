# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:37:49 2016

@author: sliu
"""

import comp_prob_inference

comp_prob_inference.flip_fair_coin()





prob_W_T_dict = {}
for w in {'sunny', 'rainy', 'snowy'}:
     prob_W_T_dict[w] = {}

prob_W_T_dict['sunny']['hot'] = 3/10
prob_W_T_dict['sunny']['cold'] = 1/5
prob_W_T_dict['rainy']['hot'] = 1/30
prob_W_T_dict['rainy']['cold'] = 2/15
prob_W_T_dict['snowy']['hot'] = 0
prob_W_T_dict['snowy']['cold'] = 1/3
comp_prob_inference.print_joint_prob_table_dict(prob_W_T_dict)
print (prob_W_T_dict)

        
#alice hunt dragons

firepower = (1,2,4)
roarvol = (1,3)
c = 0
for x in firepower:
    for y in roarvol:
        c += x*x + y*y
print(c)

dic ={}
for i in firepower:
    dic[i] = {}
    for j in roarvol:
            dic[i][j] = i*i + j*j

print (dic)

for i in firepower:
    dic[i] = {}
    for j in roarvol:
        if j < i:
            dic[i][j] = i*i + j*j

print (dic)

for i in range(1,4):
    dic[i] = {}
    for j in range(1,5):
        if j == 3:
            dic[i][j] = 0
        elif j > i:
            dic[i][j] = i*i + j*j

print (dic)

#
#
#dic = {}
#
#dic[2] = 1/36
#dic[3] = 2/36
#dic[4] = 3/36
#dic[5] = 4/36
#dic[6] = 5/36
#dic[7] = 6/36
#dic[8] = 5/36
#dic[9] = 4/36
#dic[10] = 3/36
#dic[11] = 2/36
#dic[12] = 1/36
#
#
#print (dic)
#print (dic.values())
#
#sum = 0
#for i in dic.values():
#    sum += i
#    
#print(sum)
