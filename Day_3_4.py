# pizza order app
print("Welcome to Python Pizza Deliveries!")
Size = input("What size pizza do you want? S , M or L  : ")
Add_papperoni = input("Would you like to add papperoni to your Pizza? Y or N : ")
Extra_cheese = input("Would you like to add extra cheese to your Pizza? Y or N : ")

bill = 0

if Size == "S":
    bill += 15
elif Size == "M":
    bill +=20
else:
    bill += 25

if Add_papperoni == "Y":
    if Size == "S":
        bill += 2
    else:
        bill += 3

if Extra_cheese == "Y":
    bill +=1

print(f"Your final bill is ${bill}")



