#!/usr/bin/python3

def fibonacci_generator(n):
    """Generate the first n Fibonacci numbers"""
    if n <= 0:
        return []

    fib_series = [0, 1] if n > 1 else [0]

    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)

    return fib_series

def get_positive_integer_input(prompt):
    """Get a positive integer input from the user"""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

# Get user input for the number of Fibonacci numbers to generate
n = get_positive_integer_input("Enter the number of Fibonacci numbers to generate: ")
fib_numbers = fibonacci_generator(n)
print(f"Fibonacci series of length {n}: {fib_numbers}")

