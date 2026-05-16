use std::time::Instant;

fn main() {
    println!("Fibonacci Benchmark Suite - Rust Implementation");
    
    // Test different values
    let test_values = [10, 20, 30, 40, 50];
    
    for &n in &test_values {
        println!("\nCalculating Fibonacci({})...", n);
        
        // Iterative method
        let start = Instant::now();
        let result_iter = fibonacci_iterative(n);
        let duration_iter = start.elapsed();
        println!("Iterative: {} (took {:?})", result_iter, duration_iter);
        
        // Memoized method
        let start = Instant::now();
        let result_memo = fibonacci_memoized(n);
        let duration_memo = start.elapsed();
        println!("Memoized: {} (took {:?})", result_memo, duration_memo);
        
        // Matrix exponentiation method
        let start = Instant::now();
        let result_matrix = fibonacci_matrix(n);
        let duration_matrix = start.elapsed();
        println!("Matrix: {} (took {:?})", result_matrix, duration_matrix);
    }
}

/// Iterative implementation of Fibonacci with O(n) time and O(1) space complexity
fn fibonacci_iterative(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    
    let mut a = 0u64;
    let mut b = 1u64;
    
    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    
    b
}

/// Memoized implementation using a cache
fn fibonacci_memoized(n: u64) -> u64 {
    let mut cache = std::collections::HashMap::new();
    fib_memo_helper(n, &mut cache)
}

fn fib_memo_helper(n: u64, cache: &mut std::collections::HashMap<u64, u128>) -> u64 {
    if n <= 1 {
        return n;
    }
    
    if let Some(&cached) = cache.get(&n) {
        return cached as u64;
    }
    
    let result = fib_memo_helper(n - 1, cache) as u128 + fib_memo_helper(n - 2, cache) as u128;
    cache.insert(n, result);
    result as u64
}

/// Matrix exponentiation implementation - O(log n) time complexity
fn fibonacci_matrix(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    
    let base_matrix = [[1u64, 1u64], [1u64, 0u64]];
    let result_matrix = matrix_power(base_matrix, n - 1);
    result_matrix[0][0]
}

/// Helper function to multiply two 2x2 matrices
fn matrix_multiply(a: [[u64; 2]; 2], b: [[u64; 2]; 2]) -> [[u64; 2]; 2] {
    [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ],
    ]
}

/// Helper function to compute matrix^n using fast exponentiation
fn matrix_power(matrix: [[u64; 2]; 2], n: u64) -> [[u64; 2]; 2] {
    if n == 1 {
        return matrix;
    }
    
    if n % 2 == 0 {
        let half_power = matrix_power(matrix, n / 2);
        return matrix_multiply(half_power, half_power);
    }
    
    matrix_multiply(matrix, matrix_power(matrix, n - 1))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fibonacci_iterative() {
        assert_eq!(fibonacci_iterative(0), 0);
        assert_eq!(fibonacci_iterative(1), 1);
        assert_eq!(fibonacci_iterative(2), 1);
        assert_eq!(fibonacci_iterative(3), 2);
        assert_eq!(fibonacci_iterative(10), 55);
        assert_eq!(fibonacci_iterative(20), 6765);
    }

    #[test]
    fn test_fibonacci_memoized() {
        assert_eq!(fibonacci_memoized(0), 0);
        assert_eq!(fibonacci_memoized(1), 1);
        assert_eq!(fibonacci_memoized(2), 1);
        assert_eq!(fibonacci_memoized(3), 2);
        assert_eq!(fibonacci_memoized(10), 55);
        assert_eq!(fibonacci_memoized(20), 6765);
    }

    #[test]
    fn test_fibonacci_matrix() {
        assert_eq!(fibonacci_matrix(0), 0);
        assert_eq!(fibonacci_matrix(1), 1);
        assert_eq!(fibonacci_matrix(2), 1);
        assert_eq!(fibonacci_matrix(3), 2);
        assert_eq!(fibonacci_matrix(10), 55);
        assert_eq!(fibonacci_matrix(20), 6765);
    }

    #[test]
    fn test_consistency_between_methods() {
        let test_values = [0, 1, 2, 3, 5, 10, 15, 20];
        
        for &n in &test_values {
            let iter_result = fibonacci_iterative(n);
            let memo_result = fibonacci_memoized(n);
            let matrix_result = fibonacci_matrix(n);
            
            assert_eq!(iter_result, memo_result, "Mismatch at n={} between iterative and memoized", n);
            assert_eq!(iter_result, matrix_result, "Mismatch at n={} between iterative and matrix", n);
        }
    }
}