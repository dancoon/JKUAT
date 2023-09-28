#!/usr/bin/python3
"""
Ian Dancun Mwangi SCT211-0005/2022
"""

def calculator():
    name = input('Enter your name: ')
    print(f"Hello, {name}.")
    num_one = input('Enter the first number: ')
    num_two = input('Enter the second number: ')
    try:
        ans = eval(f"{num_one} + {num_two}")
        print(f"The sum of {num_one} and {num_two} is {ans}")
    except Exception as e:
        print("Invalid numbers !!!")

if __name__ == "__main__":
    calculator()
