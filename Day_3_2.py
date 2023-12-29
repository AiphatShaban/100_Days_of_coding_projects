height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kgs: "))

BMI =round((weight)/(height)**2)

if BMI < 18.5 :
    print(f"your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you have are  overweight")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you have are obese")
else:
    print(f"Your BMI is {BMI}, you have a clinicaly obese")

    



