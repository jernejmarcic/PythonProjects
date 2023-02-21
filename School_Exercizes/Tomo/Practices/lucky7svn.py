count = 0
num = 1
while num <= 250:
    if num % 7 == 0:
        count += 1
    num += 1

print("Number of integers between 1 and 250 divisible by 7:", count)