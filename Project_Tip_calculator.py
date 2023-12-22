# A Tip calculator that calculates how much each person should pay

print("Welcome to Tip calculator!")
bill=int(input("What was the total bill? shs."))
tip =int(input("What percentage tip would you like to give? 10, 12 , or 15?"))
people=int(input("How many people to split the bill?"))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)

# the second final_amount is to ensure that we get the corresponding number of decimals even when the last digit in the decimal is zero
final_amount ="{:.2f}".format(bill_per_person)
print(f"Each person should pay: shs {final_amount}")