const memo = new Map();

function fibonacci(n) {
    // Check if value is already computed
    if (memo.has(n)) {
        return memo.get(n);
    }

    // Base cases
    if (n <= 1) {
        memo.set(n, n);
        return n;
    }

    // Recursive calculation
    const result = fibonacci(n - 1) + fibonacci(n - 2);
    memo.set(n, result);
    return result;
}

module.exports = { fibonacci };

// Only run main if this file is executed directly
if (require.main === module) {
    function main() {
        const args = process.argv.slice(2);
        
        if (args.length !== 1) {
            console.error("Usage: node fibonacci.js <n>");
            process.exit(1);
        }
        
        const n = parseInt(args[0], 10);
        if (isNaN(n)) {
            console.error("Error: Please provide a valid number");
            process.exit(1);
        }
        
        if (n < 0) {
            console.error("Error: Fibonacci is not defined for negative numbers");
            process.exit(1);
        }
        
        const result = fibonacci(n);
        console.log(`F(${n}) = ${result}`);
    }

    main();
}