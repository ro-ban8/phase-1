
 
while True:
   try:
      height = float(input("what is your height in meters " ))
      weight = float(input("what is your wight in kg "))
   except ValueError:
       pass
   else:
      break        
def square(height):
    return height * height
BMI = weight / square(height)
print(f"Your BMI is: {BMI:.2f}")
