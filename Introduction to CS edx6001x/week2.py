# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:03:39 2016

@author: sliu
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    n = len(aStr)
    mid = int(n/2)
    if n <=0:
        return False
    elif n == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[:mid])
        else:
            return isIn(char, aStr[mid+1:])
    


#guess my number

#print ('Please think of a number between 0 and 100!')
#
#h = 100
#l = 0
#guess = (h+l)/2
#
#
#
#x = 0
#while x != 'c':
#	print ('Is your secret number ' + str(guess) +'?')
#	x = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
#
#	if x not in ['h', 'l', 'c']:
#		print('Sorry, I did not understand your input.')
#		continue
#	if x == 'l':
#		l = guess
#		guess = int((h+l)/2)
#	elif x == 'h':
#		h = guess
#		guess = int((h+l)/2)
#	else:
#		print ('Game over. Your secret number was: ' + str(guess))
#		break
#
#
## Test Case 1:
#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
#
#def remainingb(b, r, mr):
#    for i in range(1, 13):
#        payment = b * mr
#        b = (b-payment) * (1+r/12)
#        # print ('Month ' + str(i) +' Remaining Balance' + str(round(b,2)))
#    print ('Remaining balance: ' + str(round(b,2)))
#
##remainingb(balance, annualInterestRate, monthlyPaymentRate)
##remainingb(484,0.2,0.04)
#
#def fixedP(b, r):
#    lowestP = round(b/120,0)*10
#    temp = b
#    while b > 0:
#        b = temp
#        for i in range(1,13):
#            b = (b-lowestP) * (1+r/12)
#        if b >=120:
#            lowestP += round(b/120,0)*10
#        elif b<0:
#            break
#        else:
#            lowestP =+10
#    print ('Lowest Payment: ' + str(lowestP))
#
#fixedP(3926, 0.2)
#
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#        if iteration % 2 == 0:
#            break
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
  
#  
#def fixedP(b, r):
#    lowestP = b/12
#    maxP = b*((1+r/12)**12)/12
#    remainingb = b
#    p = (lowestP + maxP)/2
#    while abs(remainingb) > 1:
#        p = (lowestP + maxP)/2
#        for i in range(1,13):
#            remainingb = (remainingb - p)*(1+r/12)
#        print (remainingb)
#        if remainingb > 0:
#            lowestP = p
#        else:
#            maxP = p
#         
#    print ('Lowest Payment: ' + str(p))
#fixedP(32000, 0.2)
#
#balance = 320000
#annualInterestRate = 0.2   
#fixedP(balance, annualInterestRate)
#
#def test(i):
#    '''
#    input:i, a positive int
#    Returns True if i is even, otherwise False
#    '''
#    print ("hi")
#    return i%2 == 0
#test(256)


