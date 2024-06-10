import random
rock= '''






'''
scissors = '''



'''
paper='''




'''
user_choice=int(input("what do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice==0 and computer_choice==2:
    print("you win!!!!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice==user_choice:
    print("It's a draw!")        
else:
    print("You typed an invalid number. You lose!!")