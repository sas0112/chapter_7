sandwich_orders = ["tuna", "ham", "sausage", "apple"]
finished_sandwiches = []

# making sandwiches
print("making sandwiches now:")
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(making_sandwich)
    print("\t" + making_sandwich + " sandwich is complete!")

print("All sandwiches is made:")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
