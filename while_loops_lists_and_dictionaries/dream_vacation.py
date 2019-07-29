poll_result = {}

# name and places
poll_active = True


while poll_active:
    print("\nVery glad for you to take part in our survey")
    # input name and places
    name = input("What is your name: ")
    place = input("if you want to visit a place in the world"
                  + "\n, where would you want to go?")
    # give dictionaries values and keys
    poll_result[name] = place
    remain_people = input("is there any other one who want to do the survey?(yes/no) ")

    # decide whether to continue
    if remain_people == "yes":
        poll_active = True
    else:
        poll_active = False

print("\nLet's see our final result:")
for name,place in poll_result.items():
    print(name + " wants to go to " + place)
