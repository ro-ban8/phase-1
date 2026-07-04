def main():
   while True:

    try: 
        weight = float(input("what is your weight in kg ?  "))
        height = float(input("what is your height in meaters ? "))
    except ValueError:
        pass
    else:
        BMI = weight/square(height)
        print (f"Your BMI is {BMI:.2f} kg/sq.m ")
        break   

def square(height):
      return height * height

main()