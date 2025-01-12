def sponge_case(input_string):
    result = ''
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result += char.lower()  # Even index: lowercase
        else:
            result += char.upper()  # Odd index: uppercase
    return result

# Get user input
input_string = input("Enter a string: ")
result_string = sponge_case(input_string)
print(f"SpongeCase version: {result_string}")
