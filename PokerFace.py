import numpy as np
import random

#Initializing the list cards_Received
cards_Received = np.zeros(100000)
#print(cards_Received)

#Poker hand simulation

i = 0
for i in range(len(cards_Received)):
    board = np.zeros((13,4))
    k = 0
    while k < 5:
        a = random.randint(0,12)
        b = random.randint(0,3)
        if board[a][b] == 1:#make sure no repeat
            continue
        else:
            board[a][b] = 1
        k += 1
    #print(board)
    for j in range(len(board)):
        if sum(board[j]) >= 2:
            cards_Received[i] = 1

print(sum(cards_Received)/100000)