#!/usr/bin/python3
"""
Ian Dancun Mwangi SCT211-0005/2022
"""

def calculator():
    bill = float(input("Enter the total bill amount: Ksh "))
    tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
    num_people = int(input("Enter the number of people splitting the bill: "))

    if tip_percentage not in [10, 12, 15]:
        print("Invalid tip percentage. Please enter 10, 12, or 15.")
        return
    
    tip_amount = bill * (tip_percentage / 100)
    total_amount = bill + tip_amount
    amount_per_person = total_amount / num_people

    print(f"Each person should pay: Ksh {amount_per_person:.2f}")


if __name__ == "__main__":
    calculator()