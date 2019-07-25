import random

occupied_seat = random.randint(1,20)

print("Welcome! I'm going to check whether there are spare tables")
print("Now there are " + str(occupied_seat) + " guests are currently in the restaurant")
if occupied_seat > 8:
    print("Sorry, but you have to wait for another seat.")
else:
    print("Your table is ready!")