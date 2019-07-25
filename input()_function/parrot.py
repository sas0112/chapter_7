prompt = "If you tell me who you are, we can personalize the messages for you, "
prompt += "\nWhat is your name: "

name = input(prompt)
print("Hello: " + name.title() + "\n")

prompt_age = "And now, how old are you? "
age = input(prompt_age)
print("You are " + age + " years old." + "\n")

if int(age)  >= 18:
    print("You have grown up!")
else:
    print("You are not old enough！")