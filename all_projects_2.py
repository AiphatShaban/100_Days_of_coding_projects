# the first project = band name generator

print("Welcome to the band name generator!")
city=input("where do you come from?  ")
pet =input("What's your pet's name?  ")
Band_name = print("The band name is"   +  city + " " + pet)

# the second project = BMI calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in kgs: ")

BMI = int(weight)//float(height)**2

print(BMI)


# life in weeks project
# 1YR =365 days, 1yr= 52 weeks , 1 yr= 12 months

Age = input("what's your current age?")

Age_as_int =int(Age)

years_remaining = 90 - Age_as_int
Months_remaining = years_remaining*12
weeks_remaining = years_remaining*52
days_remaining = years_remaining*365

message= f"You have {days_remaining} days,{weeks_remaining} weeks and {Months_remaining} months left"
print(message)

# tip calculator project 3

print("Welcome to the tip calculator!")
bill =float(input("What was the total bill? shs "))
tip = int(input("How much tip would you like to give? 10,12 or 15?  "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount ="{:.2f}".format(bill_per_person)

print(f"Each person should pay: shs {final_amount}")
