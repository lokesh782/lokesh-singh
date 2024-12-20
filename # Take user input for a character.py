# Take user input for a character
char = input("Enter a character: ")

# Check if the character is uppercase, lowercase, or a digit
if char.isupper():
    print(f"The character '{char}' is uppercase.")
elif char.islower():
    print(f"The character '{char}' is lowercase.")
elif char.isdigit():
    print(f"The character '{char}' is a digit.")
else:
    print(f"The character '{char}' is neither uppercase, lowercase, nor a digit.")
