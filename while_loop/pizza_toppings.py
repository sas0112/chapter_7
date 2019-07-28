prompt = "Please enter the topping you want on your pizza:"
prompt += "\nIf you want to quit, simply enter 'quit'. "

topping = ""
while topping != "quit":
    topping = input(prompt)
    print(topping.title() + " is already added to your pizza!")
    continue
else:
    print("Your pizza is ready to be served.")