print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")


choice1=input('You are at the cross roads,where would you go ? Type "left" or "right" \n').lower()


if choice1 == "left":
    choice2=input("You\'ve come to a lake.There is an island in the middle of the lake. type 'wait' to wait for the boat or type 'swim' to swim across the lake.\n").lower()
    if choice2 =="wait":
        choice3 =input("You arrive at the island unharmed.There is a house with three doors.One red, one yellow and one blue. which color do you choose? \n").lower()
        if choice3 == "red":
            print("you are in a room full of fire!. Game over")
        elif choice3 == "blue":
            print("You are in a room full of beasts!. Game over")
        elif choice3 == "yellow":    
            print("You win. The treasure is all yours captain!!")
        else:
            print("You chose a room that does'nt exist!. Game over!!!")    
    else:
        print("You got attacked by crocodiles! . Game over!")    
else:
    print("You fell into a hole. Game over!")



