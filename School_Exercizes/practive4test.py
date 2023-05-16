arr = [1, 45, 54, 8, 67, 4, 7, 9, 2]
maxV = arr[0]

for i in range(len(arr)):
    if arr[i] > maxV:
        maxV = arr[i]


print(maxV)

for i in range(len(arr)):
    if arr[i] > 10:
        arr[i+i]
