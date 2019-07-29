sandwich_orders = ["tuna", "ham", "sausage", "apple", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

# eliminating pastrami
print("WE have run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# making sandwiches
print("making sandwiches now:")
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(making_sandwich)
    print("\t" + making_sandwich.title() + " sandwich is complete!")

print("All sandwiches is made:")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
