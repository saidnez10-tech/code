# Take input from the user
user_input = input("Enter a character: ")

# Check if the input is exactly 1 character and is an alphabet
if len(user_input) == 1 and user_input.isalpha():
    print(f"'{user_input}' is an alphabet.")
else:
    print(f"'{user_input}' is not an alphabet.")