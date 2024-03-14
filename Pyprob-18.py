#Problem 18: Leap Year
#Write a program that checks if a given year is a leap year.

def isLeap(num):
    if num%4==0:
        return True
    else:
        return False

year = int(input('Enter the year to check if it is leap or not: '))

year_ch= isLeap(year)

if year_ch is True:
    print('Year ', year, ' is a Leap year!')
else:
    print('Year ', year, ' is a not Leap year!')
