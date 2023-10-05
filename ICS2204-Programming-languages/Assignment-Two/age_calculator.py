#!/usr/bin/python3
"""
Ian Dancun Mwangi SCT211-0005/2022
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculator():
    name = input('Enter your name: ').strip()
    print(f"Hello, {name}.")
    date_of_birth = input("Enter you birthday in the format dd/mm/yyyy: ")
    dob = datetime.strptime(date_of_birth, "%d/%m/%Y")
    now = datetime.now()
    difference = relativedelta(now, dob)
    years = difference.years
    months = difference.months 
    days = difference.days
    print(f"{name}, you're {years} years {months} months {days} days old")

if __name__ == "__main__":
    calculator()
