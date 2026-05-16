#!/usr/bin/env python3

import time
import sys
from fibonacci import fibonacci


def benchmark_fibonacci(n):
    """Benchmark the fibonacci function for a given n"""
    start_time = time.perf_counter()
    result = fibonacci(n)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    return result, execution_time


def main():
    if len(sys.argv) != 2:
        print("Usage: python benchmark.py <n>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        result, exec_time = benchmark_fibonacci(n)
        print(f"Python Fibonacci({n}) = {result}")
        print(f"Execution time: {exec_time:.6f} seconds")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()