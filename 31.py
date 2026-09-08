# Read month number (1–12) and print number of days in that month
month = int(input("Enter month number (1-12): "))

if month == 2:
    print("28 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")
    