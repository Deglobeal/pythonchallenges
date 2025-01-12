def binary_to_decimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

# Get binary input from the user
binary_input = input("Enter a binary number: ")

# Ensure the input is a valid binary number
if binary_input.isdigit() and all(char in '01' for char in binary_input):
    # Convert the binary string to an integer
    binary_number = int(binary_input)
    decimal_result = binary_to_decimal(binary_number)
    print(f"The decimal equivalent of {binary_input} is {decimal_result}")
else:
    print("Invalid input. Please enter a valid binary number.")
