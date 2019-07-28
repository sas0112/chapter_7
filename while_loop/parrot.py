prompt = "Tell me something, and I will repeat back to you,"
prompt += "\nIf you want me to stop, simply enter 'quit'. "

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)