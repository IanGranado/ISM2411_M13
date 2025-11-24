print("Welcome to my Python program!")

hours = float(hours)
weekly_hours = hours * 7

print(f"You are on track to study {weekly_hours} hours this week.")

try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()