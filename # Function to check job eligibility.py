# Function to check job eligibility
def check_job_eligibility(age, experience):
    if age > 18 and experience >= 2:
        return "Eligible"
    else:
        return "Not Eligible"

# Input from the user
age = int(input("Enter your age: "))
experience = float(input("Enter your years of experience: "))

# Check eligibility and display result
eligibility = check_job_eligibility(age, experience)
print(f"Job Eligibility Status: {eligibility}")
