start = int(input("Enter starting hotel room number: "))
end = int(input("Enter ending hotel room number: "))
c = start - 1
while c < end:
    c += 1
    if "7" in str(c):
        print("X")

    elif int(c) % 7 == 0:
        print("X")

    else:
        print(c)


