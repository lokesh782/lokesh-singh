# Function to check movie watching eligibility
def check_movie_eligibility(age):
    if age >= 18:
        return "Allowed"
    else:
        return "Not Allowed"

# Input from the user
age = int(input("Enter your age: "))

# Check eligibility and display result
eligibility = check_movie_eligibility(age)
print(f"Movie Watching Status: {eligibility}")
