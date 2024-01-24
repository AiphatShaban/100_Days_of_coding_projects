# How to use python lists
# Banker roulette challenge
import random


names_string = input("Give me everybody's name , separted by a coma.")
names=names_string.split(",")
print(names)
# we introduce the len function to count the names 
num_items=len(names)
random_choice = random.randint(0,num_items-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay   +   "  is going to buy the meal today")

