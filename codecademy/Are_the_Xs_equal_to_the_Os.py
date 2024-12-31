#this code is to count if the Xs and Os are equals to each other 

def are_xs_equal_to_os(s):
    #Check if the number of Xs and Os in a string are equal.
    
    #    s (str): The input string.
        
    #    bool: True if the counts of Xs and Os are equal, otherwise False.
 
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    x_count = s.count('x')
    o_count = s.count('o')
    
    # Return True if counts are equal, including if both are 0
    return x_count == o_count

# Get user input and check if Xs equal Os
user_input = input("Enter a string: ")
result = are_xs_equal_to_os(user_input)
print(f"Are Xs equal to Os? {result}")
