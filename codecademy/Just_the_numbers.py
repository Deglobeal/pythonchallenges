def extract_integers_from_input():
    # Take input from the user
    input_str = input("Enter a list of mixed integers and strings (e.g., [1, 'apple', 3, 'banana']): ")
    
    # Convert the input string to an actual list
    try:
        input_list = eval(input_str)
        
        # Ensure the list is valid and contains a mix of integers and strings
        if isinstance(input_list, list):
            # Return a list with only integers, keeping the order
            result = [item for item in input_list if isinstance(item, int)]
            return result
        else:
            return "Invalid input. Please enter a list of integers and strings."
    
    except:
        return "Error in input. Please enter the list correctly."

# Example usage:
result = extract_integers_from_input()
print(result)
