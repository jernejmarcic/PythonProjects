adder = 0
counter = 0

while True:
    num1 = float(input())
    adder += num1
    counter += 1
    if num1 == 0:
        break
print(f"The average is {adder/counter}")