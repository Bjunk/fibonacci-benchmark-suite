#!/usr/bin/env python3

import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    This avoids iteration and is memory efficient due to caching.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        result = fibonacci(n)
        print(f"F({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()