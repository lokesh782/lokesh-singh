# Define the correct username and password
correct_username = "admin"
correct_password = "password123"

# Take user input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username and password are correct
if username == correct_username and password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")
