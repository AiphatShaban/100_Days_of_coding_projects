# A program that works as a BMI calculator giving out the results of a person's body mass index


height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI =int(weight)/float(height)**2
BMI_as_int = int(BMI)
print(round(BMI))