# leap year checker
year = int(input("Which year would you like to check?  "))


if  year %4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap")
    else:
        print("leap year")
else:
    print("Not leap year")    
    
