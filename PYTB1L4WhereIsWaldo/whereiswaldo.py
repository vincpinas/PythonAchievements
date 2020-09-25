import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

stoelen = ["Nr. 1", "Nr. 2", "Nr. 3", "Nr. 4", "Nr. 5", "Nr. 6", "Nr. 7", "Nr. 8",]
stoel = random.choice(stoelen)

for Waldo in people:
    if Waldo == "Waldo":
        print("Waldo zit in stoel" + " " + stoel)
        break
    else:
        print(people)
        continue