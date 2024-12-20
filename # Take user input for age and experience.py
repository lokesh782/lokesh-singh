# Take user input for age and experience
age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))

# Check eligibility based on age and experience
if age > 18 and experience >= 2:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")
