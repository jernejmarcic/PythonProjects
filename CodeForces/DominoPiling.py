"""
You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.
Input

In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).
Output

Output one number — the maximal number of dominoes, which can be placed.
"""

side1 = int(input("Enter side 1 of the board: "))
side2 = int(input("Enter side 2 of the board: "))
area = side1*side2

if area % 2 == 0:
    dominos1 = area/2
    print(f"You can fit {dominos1}")

else:
    dominos2 = int(area/2)
    remain = area % 2

    if remain % 2 == 0:
        print(f"You can fit {dominos2 + remain} dominos")

    else:
        print(f"You can fit {dominos2} domies and {remain} spaces remain")
