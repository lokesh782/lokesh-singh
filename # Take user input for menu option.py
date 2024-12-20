# Take user input for menu option
menu_option = input("Enter your menu choice (Pizza, Burger, Pasta): ").lower()

# Check the menu option and print the corresponding price
if menu_option == "pizza":
    print("Pizza: $10")
elif menu_option == "burger":
    print("Burger: $7")
elif menu_option == "pasta":
    print("Pasta: $8")
else:
    print("Invalid choice. Please choose Pizza, Burger, or Pasta.")
