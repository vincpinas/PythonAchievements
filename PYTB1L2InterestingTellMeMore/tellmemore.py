import time
import os
leeftijd = input("Hoe oud ben je?  ")
print("Ah wat mooi, je bent dus " + leeftijd + " jaar oud")

time.sleep(2)
os.system("cls")

naam = input("Wat was je naam trouwens?  ")
print("Wat een mooie naam " + naam[0] .upper() + naam[1:] .lower())

time.sleep(2)
os.system("cls")

woonplaats = input("Waar woon je " + naam[0] .upper() + naam[1:] .lower() + " ?  ")
print("Okay " + naam[0] .upper() + naam[1:] .lower() + " dus je bent " + leeftijd + " jaar oud en je woont in " + woonplaats[0] .upper() + woonplaats[1:] .lower())

time.sleep(3)
while True:
    # Restart Loop
    while True:
        raw_input = input("Heb ik gelijk of heb ik gelijk?")
        answer = raw_input
        if answer in ('y', 'Y') or ('n', 'N'):
            break
    if answer == 'y' or answer == 'Y':
            print("Ik wist wel dat ik gelijk heb, laten we dit opnieuw doen!")
            time.sleep(2.7)
            os.system("py tellmemore.py")
            break
    elif answer == 'n' or answer == 'N':
            print("Hmph, nu heb ik er geen zin meer in.")
            time.sleep(2.7)
            os.system("taskkill /IM cmd.exe")
            break
    else:
            print("Invalid Input")



