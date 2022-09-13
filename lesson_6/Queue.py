from collections import deque
from random import choices, randint, random


names = ["lisa","olle", "pelle","anna","johan"]*10
print(names)

queue = deque(maxlen=10)


while len(names): #while the lenght of of the people in name. (5)
    random_number = randint(0,10) # store random number between 1-10.
    for i in range (random_number):
        if (len(queue)):
            print(queue.pop())

    for i in range (random_number):
        if len(names):
            queue.append(names.pop())
