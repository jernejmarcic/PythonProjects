num = str(input("Etner number: "))
a = 0
b = -1

numlenght = len(num)
print(numlenght)

if numlenght % 2 == 0:
    for i in range(numlenght):

        if num[a] == num[b]:
            a += 1
            b -= 1


        else:
            print("No symetry")

            exit()


    print("Symetry achieved")

