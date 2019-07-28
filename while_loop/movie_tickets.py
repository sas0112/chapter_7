prompt = ("Please enter your age: ")
prompt += ("\nIf you want to stop, Please enter 'quit'.")

active =  True
while active:
    age = input(prompt)
    if age == "quit":
        active = False
    else:
        age =int(age)
        if age < 3:
            cost = "free"
        elif age < 12:
            cost = "10$"
        else:
            cost = "15$"
        print("your ticket cost is " + cost + ".")