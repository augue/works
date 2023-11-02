def fibonacci(n):
    fib_sequence = [0, 1]
    
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    
    while len(fib_sequence) < n:
        next_num = fib_sequence[-2] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    return fib_sequence
#hf
# Example usage:
result = fibonacci(10)
print(result)
