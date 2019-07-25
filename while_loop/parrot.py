prompt = "Tell me something, and I will repeat back to you,"
prompt += "\nIf you want me to stop, simply enter 'quit'. "

message = input(prompt)
while message != "quit":
    print(message)
    break
print("This program ends.")