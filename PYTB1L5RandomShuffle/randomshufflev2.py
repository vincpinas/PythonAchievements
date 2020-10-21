import random
def randomised():
    original = "vincent"
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised) 

for i in range(3):
    randomised()
