#!/usr/bin/python3
"""
Ian Dancun Mwangi SCT211-0005/2022
"""

# Main function
def calcultor():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Invalid input. Please enter positive values for weight and height.")
        return

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        bmi_classification = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_classification = "Normal Weight"
    else:
        bmi_classification = "Overweight"

    print(f"Your BMI is {bmi:.2f}, and falls under the category: {bmi_classification}")

if __name__ == "__main__":
    calcultor()
