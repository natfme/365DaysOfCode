# Day 11 - "525,600 minutes"

# 525,600 minutes. Now, use your newfound math skills to determine how many seconds are in a year.

"""Day 11 Challenge
How many seconds are in a year?
Use the power of breaking a program down into its parts. We could Google this, but why not make a program for this instead.

60 seconds = 1 minute

60 minutes = 1 hour

24 hours = 1 day

31 days = 1 month

12 months = 1 year

365 days = 1 year

366 day = 1 leap year (this is every four years) https://spaceplace.nasa.gov/leap-year/en/

ou can multiply a bunch of numbers to figure out how many seconds are in a year.

Use input and if statements to add the extra day for leap year.

Make the computer do all the hard work and math for you. You do the thinking beforehand.
"""

LeapYear = input("Is a leap year (Please use Y or N for yes and no.): ")
LeapYear = LeapYear.lower()

if LeapYear == "y":
    numSeconds = 366*24*60*60
elif LeapYear == "n":
    numSeconds = 365*24*60*60
else:
   print("Invalid answer, Try again")
print("Number of seconds in a year are", numSeconds)


days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute


if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
else:
  print("Number of seconds in a year are", result)

x = 10
y = 20
_ = x + y

print(_)