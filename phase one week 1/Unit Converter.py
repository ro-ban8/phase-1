x = float(input("what is your amount in cm " ))
    

def convert(x):
    return x / 100


print(f"your amount in meters is: {convert(x):.2f}")

grams = float(input("what is your amount in grams " ))

def convert(grams):
    return grams * 1000

print(f"your amount in milligrams is: {convert(grams):.2f}")

#y = float(input("what is your amount in mg " ))
#molecular_mass = float(input("what is the molecular mass of the substance in mg? "))
#def convert(y, molecular_mass):
#    return y * 1000 / molecular_mass
#print(f"your amount in milli moles is: {convert(y, molecular_mass):.2f}")