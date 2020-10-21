import time, os, sys
product = input("what product would you like to make? ")
message = product + " is in development\n"
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)
factory = []
factory.append(product)
time.sleep(1)
os.system("cls")
print("factory has finished making the product " +str(factory))
time.sleep(1.7)
print("factory is sending the " + str(factory) +" to distribution")
time.sleep(1.7)
os.system("cls")
distribution = []
distribution.append(factory.pop())
factory.clear
print("distribution is preparing the " + str(distribution) + " for sale")
time.sleep(1.7)
os.system("cls")
shop = []
shop.append(distribution.pop())
distribution.clear
print("The " + str(shop) + " is ready for sale in the shop")