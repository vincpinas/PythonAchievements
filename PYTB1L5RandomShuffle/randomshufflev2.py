import random
original = ["vincent", "grappig", "hallo"]
lengte = len(original)
i = 0

def shuffle(original):
    randomised = ''.join(random.sample(original, len(original)))
    return randomised 

while i < lengte:
    print(shuffle(original[i]))
    i += 1


