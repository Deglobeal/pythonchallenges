# calculator function 
# Perform a calculation based on the operator.
# num1 (int): The first number.
# operator (str): A mathematical operator: +, -, *, or /.
# num2 (int): The second number.


def calculator(num1, operator, num2):
    
        
        
    #  Returns:
    #    float: The result of the calculation.

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator. Use +, -, *, or /.")

# Get user input
try:
    num1 = int(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))
    
    # Perform calculation
    result = calculator(num1, operator, num2)
    print(f"The result of {num1} {operator} {num2} is {result}.")
except ValueError as e:
    print(f"Error: {e}")
