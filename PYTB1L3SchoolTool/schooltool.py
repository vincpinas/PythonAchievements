import random
week = ["maandag", "disndag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

weekdag = random.choice(week)

if weekdag == "maandag" or weekdag == "woensdag":
    print("OPSTAAN! lekker weer naar school toe.")
else:
    print("even thuis blijven vandaag.")