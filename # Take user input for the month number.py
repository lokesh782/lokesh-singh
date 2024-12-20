# Take user input for the month number
month = int(input("Enter the month number (1-12): "))

# Determine the season based on the month number
if month == 12 or month == 1 or month == 2:
    season = "Winter"
elif 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Autumn"
else:
    season = "Invalid month number"

# Output the corresponding season
print(f"The season is: {season}")
