# Fibonacci Benchmark Suite

This project implements memory-efficient Fibonacci calculations in three programming languages (Python, Rust, and Node.js) without using iterative approaches. It includes a benchmark suite to compare the performance of each implementation.

## Implementations

All implementations use recursive approaches with memoization to avoid redundant calculations while maintaining memory efficiency:

1. **Python**: Uses `@lru_cache` decorator for automatic memoization
2. **Rust**: Uses a global `HashMap` with mutex for thread-safe memoization
3. **Node.js**: Uses a `Map` object for manual memoization

## Project Structure

```
├── python/
│   ├── fibonacci.py      # Fibonacci implementation
│   └── benchmark.py      # Benchmark script
├── rust/
│   ├── src/
│   │   ├── main.rs       # Fibonacci implementation
│   │   └── bin/
│   │       └── benchmark.rs  # Benchmark script
│   └── Cargo.toml        # Rust dependencies
├── nodejs/
│   ├── fibonacci.js      # Fibonacci implementation
│   └── benchmark.js      # Benchmark script
└── benchmark_runner.py   # Main benchmark coordinator
```

## Requirements

- Python 3.6+
- Rust and Cargo (for Rust implementation)
- Node.js (for Node.js implementation)

## Usage

### Individual Language Execution

#### Python
```bash
# Calculate Fibonacci number
python python/fibonacci.py 40

# Run benchmark
python python/benchmark.py 40
```

#### Rust
```bash
# Calculate Fibonacci number
cd rust && cargo run 40

# Run benchmark
cd rust && cargo run --bin benchmark 40
```

#### Node.js
```bash
# Calculate Fibonacci number
node nodejs/fibonacci.js 40

# Run benchmark
node nodejs/benchmark.js 40
```

### Running All Benchmarks

```bash
python benchmark_runner.py 40
```

This will run all three implementations with n=40 and display a performance comparison.

## Performance Comparison

After running the benchmark suite, you'll see output similar to:

```
Running Fibonacci benchmarks for n=40

Running Python benchmark...
Python: 0.000015 seconds

Running Node.js benchmark...
Node.js: 0.000008 seconds

Running Rust benchmark...
Rust: 0.000002 seconds

All implementations correctly calculated: 102334155

Performance ranking:
1. Rust: 0.000002 seconds
2. Node.js: 0.000008 seconds
3. Python: 0.000015 seconds

Fastest implementation: Rust
```

## Key Features

- **Memory Efficient**: All implementations use memoization to store previously calculated values, preventing redundant computation
- **No Iteration**: Purely recursive implementations in all three languages
- **Thread-Safe**: Rust implementation uses mutex for safe concurrent access
- **Cross-Language Comparison**: Easy benchmarking across different runtime environments