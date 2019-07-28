prompt = "\nPlease enter the name of the city you have visited"
prompt += "\n(enter 'quit' when you have finished)"

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("I love going to " + city.title() + '!')