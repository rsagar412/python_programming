# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.


# In situations where both players choose the same object, the result will be a draw.

# COMPUTER =          S W G
#                    -1 0 1
# PLAYER   =     S -1 D W W
#                W  0 W D W
#                G  1 W W D

import random

def check(comp, user):
    if(comp == user):
        return 0
    elif(comp == 0 and user == 1):
        return -1
    elif(comp == 1 and user == 2):
        return -1
    return 1

comp = random.randint(0, 2)   #random.randint() is used to generate random numbers between a given range
user = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: "))

print("Computer chose: ", comp)
print("You chose: ", user)
score = check(comp, user)

if(score == 0):
    print("It's a draw!")
elif(score == 1):
    print("You win!")
else:
    print("Computer wins!")
