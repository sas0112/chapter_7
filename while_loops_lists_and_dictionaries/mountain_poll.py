responses = {}

# set a flag to indicate the polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response
    name = input("Whats your name?")
    response = input("Do you want to climb the mountain today")

    # store them in the dictionary
    responses[name] = response

    # find out if anyone else wants to take the poll
    repeat = input("Is there anyone else who want to take the poll(yes/no)")
    if repeat == 'no':
        polling_active = False

# polling is complete, showing result.
print("---polling results---")
for name, response in responses.items():
    if response == "yes":
        answer = "want"
    else:
        answer = "don't want"
    print(name + " " + answer + " to go climbing.")
