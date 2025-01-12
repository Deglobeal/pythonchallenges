def double_characters(input_string):
    # Return a new string with each character doubled
    return ''.join([char * 5 for char in input_string])

# Example usage:
input_string = input("Enter a string: ")
result = double_characters(input_string)
print(result)
