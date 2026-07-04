systolic = int(input("Enter the systolic reading (mmhg) : "))
diastolic = int(input("Enter the diastolic reading (mmhg) : "))

if systolic >= 180 or diastolic >= 120:
     print("You have a hypertensive crisis, seek emergency care immediately")
elif systolic >= 140 or diastolic >= 90:
     print("You have high blood pressure (hypertension) stage 2")
elif systolic >= 130 or diastolic >= 80:
     print("You have high blood pressure (hypertension) stage 1")
elif systolic >= 120 and diastolic < 80:
     print("Your blood pressure is elevated")
elif systolic < 120 and diastolic < 80:
     print("Your blood pressure is normal")


else:     print("Invalid input, please enter valid blood pressure readings")
