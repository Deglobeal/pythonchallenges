# a code that get the user input and convert it to binary

def decimal_to_binary(decimal):
   
    if decimal < 0 or decimal >= 1024:
        raise ValueError("Decimal number must be between 0 and 1,023 inclusive.")
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary if binary else "0"

# Get user input and convert it
try:
    user_input = int(input("Enter a decimal number (less than 1,024): "))
    binary_number = decimal_to_binary(user_input)
    print(f"The binary equivalent of {user_input} is {binary_number}.")
except ValueError as e:
    print(f"Error: {e}")
