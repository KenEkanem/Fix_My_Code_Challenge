#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n: int) -> None:
    """
    Prints numbers from 0 to n, inclusive, with some replaced with "Fizz", "Buzz",
    or "FizzBuzz" according to the FizzBuzz problem.

    Args:
        n (int): The maximum number to print.
    """
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    output = []
    for i in range(n + 1):
        if i % 15 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    print(" ".join(output))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./fizzbuzz.py <number>")
        print("Example: ./fizzbuzz.py 89")
        sys.exit(1)
    number = int(sys.argv[1])
    fizzbuzz(number)
