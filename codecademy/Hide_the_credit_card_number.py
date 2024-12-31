def hide_credit_card(card_number):
    
    if not card_number.isdigit() or len(card_number) < 4:
        raise ValueError("Invalid credit card number. Must be numeric and at least 4 digits long.")
    
    hidden_part = "*" * (len(card_number) - 4)
    visible_part = card_number[-4:]
    return hidden_part + visible_part

# Get user input and hide the credit card number
user_input = input("Enter your credit card number: ")
try:
    masked_card = hide_credit_card(user_input)
    print(f"Masked credit card number: {masked_card}")
except ValueError as e:
    print(f"Error: {e}")
