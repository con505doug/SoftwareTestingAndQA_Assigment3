from functions import *

def main():
    keepGoing = 'Y'
    print("Welcome to the BMI Calculator!")
    print("Below you will enter your height in feet and inches and your weight.")
    while keepGoing == 'Y':
        try:
            heightFeet = float(input("\nPlease enter your height in feet: "))
            heightInches = float(input("Please enter your height in inches: "))

        except ValueError:
            print("Please enter valid height!")
            continue

        try:
            weight = float(input("Please enter your weight: "))
        except ValueError:
            print("Please enter valid weight!")
            continue

        height = heightFeet * 12 + heightInches
    
        bmi = bmiCalculator(height, weight)
        category = categorize(bmi)

        if category == "Error":
            print("Please check accuracy of your inputs!")
        else:
            print("Your BMI is {} which puts you in the {} category.".format(bmi, category))
        
        keepGoing = input("Do you wish to continue? (Y/N): ")

main()