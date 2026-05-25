d = float(input("what is your desired amount in mg ? " ))

h = float(input("what is the amount in hand in mg ? "))

q = float(input("what is the quantity in ml ? "))
dose = (d * q) / h

print(f"your dose is: {dose:.2f}")
