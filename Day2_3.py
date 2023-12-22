# a program that calculates the number of days,weeks and months one has if our life expectancy is at 90yrs 
 


Age = input("What is your current age?\n")

Age_as_int = int(Age)

years_remaining = 90 - Age_as_int
months_remaining = years_remaining*12
weeks_remaining =years_remaining*52
days_remaining = years_remaining*365

message = f"You have {days_remaining} days,{weeks_remaining} weeks and {months_remaining} months left"
print(message)