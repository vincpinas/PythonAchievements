print()

while True:
    answer = input("Did you eat breakfast today?")
    while True:
        if answer == "yes" or answer == "YES" or answer == "Y" or answer == "y":
            print("Nice, remember breakfast is the most important meal of the day!")
            break
        elif answer == "no" or answer == "NO" or answer == "N" or answer == "n":
            print("Oh, that's not good at all, remember to eat breakfast next time!")
            break
        else: 
            ("Invalid Input")