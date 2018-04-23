

year = int(input('Enter year 0000:'))


if (year % 4) == 0:  #when year divided by 4 completly it's leap year
     print("{0} is a leap year".format(year))

else:
   print("{0} is not a leap year".format(year))