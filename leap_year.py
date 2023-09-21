# Write a program to check if a given year is a leap year using a while loop.
# year = int(input("enter the year: "))
# if (year % 400==0) or (year != 100) and (year%4):
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

# import calendar
# year = int(input("Enter the year: "))
# print(calendar.isleap(year))

year = int(input("Enter a year: "))

is_leap_year = False

while year > 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap_year = True
        break
    year -= 1

if is_leap_year:
    print(f"{year + 1} is a leap year.")
else:
    print(f"{year + 1} is not a leap year.")
