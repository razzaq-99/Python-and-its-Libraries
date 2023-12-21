
                                     # Factorial
# def factorial(n):
#     if(n==0 or n==1):
#      return 1
#     else:
#         return n * factorial(n-1)
    
    
# print(factorial(4))   
# print(factorial(0)) 



                                     # Fibonacci Series

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def generate_fibonacci_series(n):
    fib_series = [fibonacci_recursive(i) for i in range(n)]
    return fib_series

def main():
    # Get user input for the length of the Fibonacci series
    n = int(input("Enter the number of terms for the Fibonacci series: "))

    # Generate and print the Fibonacci series
    result = generate_fibonacci_series(n)
    print(f"Fibonacci series with {n} terms: {result}")

if __name__ == "__main__":
    main()                                     