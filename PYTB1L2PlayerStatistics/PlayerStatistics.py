import time
import os

name = "name: "
speed = "speed: "
power = "power: "
ability = "ability: "

name1 = "Vincent Pinas"
speed1 = "150"
power1 = "170"
ability1 = "Teleportation"

name2 = "Jordan Ross"
speed2 = "700"
power2 = "10"
ability2 = "Overdrive"

name3 = "Robin Zhao"
speed3 = "159"
power3 = "140"
ability3 = "Happy Go Lucky"

name4 = "Bart de Boer"
speed4 = "129"
power4 = "600"
ability4 = "Knowledge Bomb"

print("There are 4 options presented to you here, choose which player")
print("A: Vincent Pinas")
print("B: Jordan Ross")
print("C: Robin Zhao")
print("D: Bart de Boer")
print("Pick one option"  + " " + "[A/B/C/D]: ")

raw_input = input()
while True:
    # Choice
    while True:
        answer = raw_input
        if answer in ('a', 'A') or ('b', 'B') or ('c', 'C') or ('d', 'D'):
            break
    if answer == 'a' or answer == 'A':
        time.sleep(0.3)
        print(name + name1)
        print(speed + speed1 + " " + "km/s")
        print(power + power1 + " " +"N")
        print(ability + ability1)
        break
    elif answer == 'b' or answer == 'B':
        time.sleep(0.3)
        print(name + name2)
        print(speed + speed2 + " " + "km/s")
        print(power + power2 + " " + "N")
        print(ability + ability2)
        break
    elif answer == 'c' or answer == 'C':
        time.sleep(0.3)
        print(name + name3)
        print(speed + speed3 + " " + "km/s")
        print(power + power3 + " " + "N")
        print(ability + ability3)
        break
    elif answer == 'd' or answer == 'D':
        time.sleep(0.3)
        print(name + name4)
        print(speed + speed4 + " " + "km/s")
        print(power + power4 + " " + "N")
        print(ability + ability4)
        break
    else:
        print("Invalid input.")

time.sleep(3)
os.system("cls")
os.system("py PlayerStatistics.py")