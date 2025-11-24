## test print
print("Hello World, Welcome to my Python program!")

## requesting the hours inputted
todays_hours = input("How many hours were you working for today? ")

## converting hours into a numerical float value.
## verifies that a number, and only a number, is given.
try:
    todays_hours = float(todays_hours)
except ValueError:
    print("Uh-Oh, only numeric values are accepted! Try again using numbers only.")
    exit()

##Multiplication
weekly_total = (todays_hours * 7) ##fixed multiplier

## Final result. Rounded down to two decimals as my payroll does.
print(f"Based off your input, if you work the same hours daily (for 7 days), you are on track to work {weekly_total:.2f} hours this week.")