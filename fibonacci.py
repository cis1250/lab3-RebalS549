#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def fibonacci_sequence():
    while True:
        user_input = input("How many terms of the Fibonacci sequence do you want? ")

        # Validate input
        if not user_input.isdigit():
            print("Please enter a positive integer.")
            continue

        n = int(user_input)
        if n <= 0:
            print("Please enter a positive integer.")
            continue

        # Generate Fibonacci sequence
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()  # new line after sequence
        break


# Run the program
fibonacci_sequence()
