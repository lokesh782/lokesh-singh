# Take user input for age
age = int(input("Enter your age: "))

# Categorize the age
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
else:
    category = "Adult"

# Display the category
print(f"You are a {category}.")
