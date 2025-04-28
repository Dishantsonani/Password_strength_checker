# Ask user to enter password
password = input("Enter your password: ")

# Set counters
has_upper = False
has_lower = False
has_number = False
has_special = False

# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_number = True
    else:
        has_special = True

# Check length
is_long = len(password) >= 8

# Final decision
if is_long and has_upper and has_lower and has_number and has_special:
    print("Strong Password 🔥")
elif is_long and (has_upper or has_lower) and (has_number or has_special):
    print("Moderate Password ⚡")
else:
    print("Weak Password ❌")

# Wait before closing
input("Press Enter to exit...")

