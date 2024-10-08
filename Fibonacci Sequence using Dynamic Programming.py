def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Create an array to store Fibonacci numbers up to n
    fib = [0] * (n + 1)
    fib[0] = 0  # F(0)
    fib[1] = 1  # F(1)

    # Fill the array using the bottom-up approach
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example usage
print(fibonacci(5))    
print(fibonacci(10))  
print(fibonacci(0))   
print(fibonacci(1000))  
