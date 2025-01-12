def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c = 0, 1, 1  # First three terms
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c  # Calculate next term
        return c

# Example usage:
n = int(input("Enter the value of n: "))
result = tribonacci(n)
print(f"The {n}th number in the Tribonacci sequence is: {result}")
