def calculate_discount(price, discount_percentage):
   
    if price < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Price must be non-negative and discount percentage must be between 0 and 100.")
    
    discount_amount = (price * discount_percentage) / 100
    discounted_price = price - discount_amount
    return discounted_price

# Example usage
try:
    price = int(input("Enter the full price of the item: "))
    discount_percentage = int(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percentage)
    print(f"The price after a {discount_percentage}% discount is: {final_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")
