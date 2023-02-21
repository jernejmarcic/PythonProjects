import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
roll = dice1 + dice2
print(roll)
if roll == 7 or roll == 11:
    print("You win!")

elif roll == 2 or roll == 3 or roll == 12:
    print("You lose!")

