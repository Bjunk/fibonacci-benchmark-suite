#!/usr/bin/env python3

import subprocess
import time
import sys
import os


def run_python_benchmark(n):
    """Run Python Fibonacci benchmark"""
    start_time = time.perf_counter()
    result = subprocess.run([
        sys.executable, 
        os.path.join(os.path.dirname(__file__), "python", "benchmark.py"), 
        str(n)
    ], capture_output=True, text=True)
    end_time = time.perf_counter()
    
    if result.returncode != 0:
        raise Exception(f"Python benchmark failed: {result.stderr}")
    
    # Parse the output to extract execution time
    lines = result.stdout.strip().split('\n')
    fib_result = lines[0].split('=')[1].strip()
    exec_time = float(lines[1].split(':')[1].strip().split()[0])
    
    return fib_result, exec_time


def run_nodejs_benchmark(n):
    """Run Node.js Fibonacci benchmark"""
    start_time = time.perf_counter()
    result = subprocess.run([
        "node", 
        os.path.join(os.path.dirname(__file__), "nodejs", "benchmark.js"), 
        str(n)
    ], capture_output=True, text=True)
    end_time = time.perf_counter()
    
    if result.returncode != 0:
        raise Exception(f"Node.js benchmark failed: {result.stderr}")
    
    # Parse the output to extract execution time
    lines = result.stdout.strip().split('\n')
    fib_result = lines[0].split('=')[1].strip()
    exec_time = float(lines[1].split(':')[1].strip().split()[0])
    
    return fib_result, exec_time


def run_rust_benchmark(n):
    """Run Rust Fibonacci benchmark"""
    # First build the Rust project
    build_result = subprocess.run([
        "cargo", "build", "--release", "--bin", "benchmark"
    ], cwd=os.path.join(os.path.dirname(__file__), "rust"), capture_output=True, text=True)
    
    if build_result.returncode != 0:
        raise Exception(f"Rust build failed: {build_result.stderr}")
    
    # Run the benchmark
    start_time = time.perf_counter()
    result = subprocess.run([
        "./target/release/benchmark", str(n)
    ], cwd=os.path.join(os.path.dirname(__file__), "rust"), capture_output=True, text=True)
    end_time = time.perf_counter()
    
    if result.returncode != 0:
        raise Exception(f"Rust benchmark failed: {result.stderr}")
    
    # Parse the output to extract execution time
    lines = result.stdout.strip().split('\n')
    fib_result = lines[0].split('=')[1].strip()
    exec_time = float(lines[1].split(':')[1].strip().split()[0])
    
    return fib_result, exec_time


def main():
    if len(sys.argv) != 2:
        print("Usage: python benchmark_runner.py <n>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        print(f"Running Fibonacci benchmarks for n={n}\n")
        
        # Run all benchmarks
        results = {}
        
        print("Running Python benchmark...")
        python_result, python_time = run_python_benchmark(n)
        results['Python'] = (python_result, python_time)
        print(f"Python: {python_time:.6f} seconds")
        
        print("\nRunning Node.js benchmark...")
        node_result, node_time = run_nodejs_benchmark(n)
        results['Node.js'] = (node_result, node_time)
        print(f"Node.js: {node_time:.6f} seconds")
        
        print("\nRunning Rust benchmark...")
        rust_result, rust_time = run_rust_benchmark(n)
        results['Rust'] = (rust_result, rust_time)
        print(f"Rust: {rust_time:.6f} seconds")
        
        # Verify all implementations give the same result
        all_results = [python_result, node_result, rust_result]
        if len(set(all_results)) > 1:
            print("\nWARNING: Not all implementations produced the same result!")
            for lang, (result, _) in results.items():
                print(f"{lang}: {result}")
        else:
            print(f"\nAll implementations correctly calculated: {python_result}")
        
        # Determine fastest implementation
        sorted_results = sorted(results.items(), key=lambda x: x[1][1])
        print(f"\nPerformance ranking:")
        for i, (language, (_, time)) in enumerate(sorted_results, 1):
            print(f"{i}. {language}: {time:.6f} seconds")
            
        fastest = sorted_results[0][0]
        print(f"\nFastest implementation: {fastest}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Benchmark error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()