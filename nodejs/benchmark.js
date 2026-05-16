#!/usr/bin/env node

const { fibonacci } = require('./fibonacci.js');

function benchmarkFibonacci(n) {
    const startTime = process.hrtime.bigint();
    const result = fibonacci(n);
    const endTime = process.hrtime.bigint();
    
    const executionTime = Number(endTime - startTime) / 1e9; // Convert to seconds
    return { result, executionTime };
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.length !== 1) {
        console.error("Usage: node benchmark.js <n>");
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
    
    const { result, executionTime } = benchmarkFibonacci(n);
    console.log(`Node.js Fibonacci(${n}) = ${result}`);
    console.log(`Execution time: ${executionTime.toFixed(6)} seconds`);
}

main();