def check_sorted_order(input_list):
    if input_list == sorted(input_list):
        return "The list is sorted in ascending order."
    elif input_list == sorted(input_list, reverse=True):
        return "The list is sorted in descending order."
    else:
        return "The list is not sorted."

# Example usage:
input_str = input("Enter a list of numbers (e.g., [1, 2, 3]): ")
try:
    input_list = eval(input_str)  # Convert input string to a list
    if isinstance(input_list, list) and all(isinstance(i, (int, float)) for i in input_list):
        result = check_sorted_order(input_list)
        print(result)
    else:
        print("Please enter a valid list of numbers.")
except:
    print("Invalid input. Please enter a list of numbers.")
