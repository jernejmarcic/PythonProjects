"""
Create a program that prints a christmas tree of varying height using starts *

Example:
Tree with heigh 3
*
**
***
"""
import os
os.get_terminal_size()

height = int(input("How tall do you want you tree to be(enter numbers): "))
h=1
for i in range(0, height):
    z = str(" * ")
    print(f"{z*h}".center(os.get_terminal_size().columns))
    h += 1
