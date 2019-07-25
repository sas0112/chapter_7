number = input("Enter a number and i will tell you whether this number is divisible by ten:")
number = int(number)

if number % 10 == 0:
    message = "divisible"
else:
    message = "not divisible"

print("This number is " + message + " by ten!")