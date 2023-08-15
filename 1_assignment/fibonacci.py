#!/usr/bin/python3

def fibonacci_series(n):
    """
    Implement a fibonacci series generator.
    """
    fib_series = [0,1] # Initialize the first and second number of the fibonacci_series
    while len(fib_series) < n: #Loop through the length of the fibonacci_series until it is less than n
        next_fib = fib_series[-1] + fib_series[-2] #Calculate the series by summing the last two numbers in the series
        fib_series.append(next_fib) # Append the next two numbers to the series
    return fib_series # Return the fibonacci series generated

# Testcases
print(fibonacci_series(1))
print(fibonacci_series(3))
print(fibonacci_series(8))
print(fibonacci_series(12))
