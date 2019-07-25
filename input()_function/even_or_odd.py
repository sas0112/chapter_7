number = input("Enter a number and i will tell you whether this number is even or odd:")
number = int(number)

if number % 2 == 0:
    message = "even"
else:
    message = "odd"

print("This is an " + message + " number!")