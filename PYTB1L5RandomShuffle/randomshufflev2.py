import random
original = ["vincent", "heerlijk", "smakelijk"]

randomised = ''.join(random.sample(original[0], len(original[0])))
randomised2 = ''.join(random.sample(original[1], len(original[1])))
randomised3 = ''.join(random.sample(original[2], len(original[2])))

def shuffle(randomised):
    print(randomised, randomised2, randomised3)
    return 3 * randomised 

shuffle(randomised)


