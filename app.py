print("Hello World, Welcome to my Python program!")

todays_hours = input("How many hours were you working for today? ")

try:
    todays_hours = float(todays_hours)
except ValueError:
    print("Uh-Oh, only numeric values are accepted! Try again using numbers only.")
    exit()

weekly_total = todays_hours * 7

print(f"Based off your input, if you work the same hours daily (for 7 days), you are on track to work {todays_hours:.2f} hours this week.")