# finnaly had the energy to properly do this exercize

monthstring = "JanFebMarAprMayJunJulAugSepOctNovDec"

input = int(input("Enter the month number: "))

print(monthstring[input * 3 - 3] + monthstring[input * 3 - 2] + monthstring[input * 3 - 1])