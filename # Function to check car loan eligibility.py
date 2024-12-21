# Function to check car loan eligibility
def check_loan_eligibility(salary, credit_score):
    if salary >= 50000 and credit_score >= 700:
        return "Eligible"
    else:
        return "Not Eligible"

# Input from the user
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

# Check eligibility and display result
eligibility = check_loan_eligibility(salary, credit_score)
print(f"Loan Eligibility Status: {eligibility}")
