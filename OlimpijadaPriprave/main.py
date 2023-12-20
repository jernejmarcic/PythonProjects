from math import sqrt
import numpy as np
from random import randint
def isPrime(n):
    # Corner case
    if (n <= 1):
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True

# ANSI escape codes for colors
RED = "\033[91m"
ORANGE = "\033[93m"
ENDC = "\033[0m"  # Resets the color to default


InputFile = open("./INPUT.txt",'r') #opens file for reading text
StartingPrimeForMatrix = int(InputFile.readline()) #Reads line 1
TargetPrimeSum = int(InputFile.readline()) #Reads line after that so line 2
HighestPossibleNumber = TargetPrimeSum//2

FiveDigitPrimesArr = []
PrimeBuffer = []
StaringPrimeNumberCandiates = []
BorderPrimeNumbersArr = []

def can_be_added(number):
    for digit in str(number):
        if digit > '6':
            return False
    return True
def FiveDigitPrimesWithSum():
    i = 10000
    while True:
        i += 1
        if isPrime(i) == True:
            if sum(int(digit) for digit in str(i)) == TargetPrimeSum:
                if can_be_added(i):
                    FiveDigitPrimesArr.append(i)



        if i >= 100000:
            break




FiveDigitPrimesWithSum()
print(f"Number of candiates: {len(FiveDigitPrimesArr)}, \n"
      f"Candiates: {FiveDigitPrimesArr}")


for j in range (len(FiveDigitPrimesArr)):
    FiveDigitPrimesSumInString = str(FiveDigitPrimesArr[j])
    if "0" not in FiveDigitPrimesSumInString:
        if FiveDigitPrimesSumInString[0] == "1":
            StaringPrimeNumberCandiates.append(FiveDigitPrimesArr[j])


for k in range (len(FiveDigitPrimesArr)):
    FiveDigitPrimesSumInString = str(FiveDigitPrimesArr[k])
    if "0" not in FiveDigitPrimesSumInString and "2" not in FiveDigitPrimesSumInString and "4" not in FiveDigitPrimesSumInString:
        BorderPrimeNumbersArr.append(FiveDigitPrimesArr[k])



print(f"Number of starter candiates: {len(StaringPrimeNumberCandiates)}, \n"
      f"Starter Candiates: {StaringPrimeNumberCandiates}")

print(f"Number of Border candiates: {len(BorderPrimeNumbersArr)}, \n"
      f"Border Candiates: {BorderPrimeNumbersArr}")


if (isPrime(TargetPrimeSum) == True) and (isPrime(StartingPrimeForMatrix) == True or StartingPrimeForMatrix == 1) and (StartingPrimeForMatrix < TargetPrimeSum+2):
    StartingRandomPositionInArrays = randint(len(StaringPrimeNumberCandiates))
    BorderRandomPositionInArrays = randint(len(BorderPrimeNumbersArr))
    np.array([[

    ]])



else:
    print(f"{RED}Error{ENDC}: Invalid input values. {ORANGE}TargetPrimeSum{ENDC} and {ORANGE}StartingPrimeForMatrix{ENDC} must be prime, and {ORANGE}StartingPrimeForMatrix{ENDC} must be less than {ORANGE}TargetPrimeSum{ENDC}.")

