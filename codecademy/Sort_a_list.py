def sort_list(numbers, order):
    
    # Sort a list of numbers based on the specified order.
    # this code is to sort list as follows
    #    numbers (list): A list of numbers to sort.
    #    order (str): The sorting order - "asc", "desc", or "none".
        
    # and Returns:
    #    list: The sorted or original list based on the order.
    
    if order == "asc":
        return sorted(numbers)
    elif order == "desc":
        return sorted(numbers, reverse=True)
    elif order == "none":
        return numbers
    else:
        raise ValueError("Invalid. Please use 'asc', 'desc', or 'none'.")

# Example usage:
numbers_list = [3, 1, 4, 1, 5, 9]
order_type = "asc"  # Replace with "asc", "desc", or "none"
result = sort_list(numbers_list, order_type)
print(f"Sorted list: {result}")
