#!/usr/bin/python3
"""
Ian Dancun Mwangi SCT211-0005/2022
"""

def main():
    year = int(input("Enter year: "))
    if year % 4 == 0:
        print(f"The {year} is a leap year.")
    else:
        print(f"The {year} is not a leap year.")

if __name__ == "__main__":
    main()