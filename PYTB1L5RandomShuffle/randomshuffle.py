import random

original1 = "hallo"
original2 = "doei"
original3 = "okay"
randomised = ''.join(random.sample(original1, len(original1)))
print(randomised)
randomised = ''.join(random.sample(original2, len(original2)))
print(randomised)
randomised = ''.join(random.sample(original3, len(original3)))
print(randomised)