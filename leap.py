from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Get the ending year from the user
end_year = int(input("Enter a year: "))

# Loop from current year to the entered year (inclusive)
for year in range(current_year, end_year + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
