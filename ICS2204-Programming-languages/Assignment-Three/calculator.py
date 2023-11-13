#!/usr/bin/python3
"""
Ian Dancun Mwangi SCT211-0005/2022
"""
from datetime import datetime

from dateutil.relativedelta import relativedelta


class Calculator:
    def __init__(self, name: str) -> None:
        self.name = name

    def add(self, num_one: int, num_two: int) -> int:
        return num_one + num_two

    def get_age(self, date_of_birth: str) -> tuple:
        dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
        difference = relativedelta(datetime.now(), dob)
        years = difference.years
        months = difference.months
        days = difference.days
        return years, months, days

    def get_bmi(self, weight: float, height: float) -> None:
        if weight <= 0 or height <= 0:
            print("Invalid input. Please enter positive values for weight and height.")
            return
        bmi = weight / (height**2)
        if bmi < 18.5:
            bmi_classification = "Underweight"
        elif 18.5 <= bmi < 24.9:
            bmi_classification = "Normal Weight"
        else:
            bmi_classification = "Overweight"
        print(
            f"Your BMI is {bmi:.2f}, and falls under the category: {bmi_classification}"
        )

    def cheack_is_leap_year(self, year: int) -> None:
        if year % 4 == 0:
            print(f"The {year} is a leap year.")
        else:
            print(f"The {year} is not a leap year.")

    def get_amount(self, bill: float, tip_percentage: int, num_people: int) -> float:
        if tip_percentage not in [10, 12, 15]:
            print("Invalid tip percentage. Please enter 10, 12, or 15.")
            return
        tip_amount = bill * (tip_percentage / 100)
        total_amount = bill + tip_amount
        amount_per_person = total_amount / num_people
        return amount_per_person


if __name__ == "__main__":
    name = input("Enter your name: ")
    num_one = int(input("Enter the first number: "))
    num_two = int(input("Enter the second number: "))
    calculator = Calculator(name=name)
    print(
        f"Hello {name},\nThe sum of {num_one} and {num_two} is {calculator.add(num_one=num_one, num_two=num_two)}"
    )
    date_of_birth = input("Enter you birthday in the format dd/mm/yyyy: ")
    years, months, days = calculator.get_age(date_of_birth=date_of_birth)
    print(f"Hello {name}, {name}, you're {years} years {months} months {days} days old")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    calculator.get_bmi(weight=weight, height=height)
    year = int(input("Enter year: "))
    calculator.cheack_is_leap_year(year=year)
    bill = float(input("Enter the total bill amount: Ksh "))
    tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
    num_people = int(input("Enter the number of people splitting the bill: "))
    print(
        f"Each person should pay: Ksh {calculator.get_amount(bill=bill, tip_percentage=tip_percentage, num_people=num_people):.2f}"
    )
