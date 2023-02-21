import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = (a**2) + (b**2)
result = math.sqrt(c)
if math.isfinite(result) and math.floor(result):
    print(f"({a}; {b}; {result})")