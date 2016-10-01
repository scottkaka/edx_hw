from ps4a import *
from ps4b import *


# x={'a':1, 'x':2, 'l':3, 'e':1}
# displayHand(x)

# print (dealHand(5))

# hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# print(updateHand(hand, 'quail'))
# print(calculateHandlen(hand))

wordList = loadWords()
# playGame(wordList)
n=5
hand = dealHand(n)
playHand(hand, wordList,n)
print (hand)

