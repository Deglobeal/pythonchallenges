def loves_me_not(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print("Loves me")
        else:
            print("Loves me not")

# Get user input
n = int(input("Enter an integer n: "))
loves_me_not(n)
