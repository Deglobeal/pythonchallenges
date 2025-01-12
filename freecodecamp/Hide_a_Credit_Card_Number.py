def mask_credit_card(card_number):
    card_number_str = str(card_number)
    # Replace all digits except the last four with asterisks
    masked_card = '*' * (len(card_number_str) - 4) + card_number_str[-4:]
    return masked_card

# Get user input
card_number = input("Enter your credit card number: ")

# Ensure the input is valid (contains only digits)
if card_number.isdigit() and len(card_number) >= 4:
    masked_card_number = mask_credit_card(card_number)
    print(f"Masked credit card number: {masked_card_number}")
else:
    print("Invalid input. Please enter a valid credit card number.")
