# This script will convert from celcious to farenheit

# The user enters what they want to convert
choice = int(input("Press 1 for celcious to faranheit and 2 for farnheit to celcious, press 3 for other options: "))

# If they enterd 1 this will run
if choice == 1:
    # This will take users input of celcious and convert it into farenheit
    celcious = float(input("Enter the temperature in Celcious: "))
    Farenhitconv = (celcious * 1.8) + 32
    print(f"In Farenheit the temperature is {Farenhitconv}")

# If they enterd 2 this will run
elif choice == 2:
    # This will take users input of farenhit and convert it into celcious
    farenheit = float(input("Enter the tempreture in Farenheit: "))
    Celciousconv = (farenheit - 32) / 1.8
    print(f"In Celcious the temperature is {Celciousconv}")

# If they enterd 3 this will run
if choice == 3:
    kelchoice = int(input("If wou want to convert between Celcious and Kelvin press 4, if you want to convert between farenheit and Kelvin press 5: "))

    if kelchoice == 4:
        convchoice = int(input("If you want to convert from Kelvin to Celcious press 6, if you want to convert form Celcious to Kelvin press 7: "))
        if convchoice == 6:
            kelvin = float(input("Enter the temperature in kelvin: "))
            keltcel = kelvin - 273.15
            print(f"The temerature in Celcious is {keltcel}")

        elif convchoice == 7:
            celcious = float(input("Enter the temperature in Celcious: "))
            celtokel = celcious + 273.15
            print(f"The temerature in Kelvin is {celtokel}")


    if kelchoice == 5:
        farchoice = int(input("If you want to convert from Kelvin to farenheit press 8, if you want to convert from farenheit to kelvin press 9: "))
        if farchoice == 8:
            kelvin1 = float(input("Enter the temperature in Kelvin: "))
            keltofar = (((kelvin1 - 279.15)*9)/5)+32
            print(f"The temerature in Kelvin is {keltofar}")


        elif farchoice == 9:
            farenheit = float(input("Enter the tempreture in Farenheit: "))
            fartokel = (farenheit + 459,67)*(5/9)
            print(f"The temerature in Farenheit is {fartokel}")




