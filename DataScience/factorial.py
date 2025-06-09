# Assignment 2: find the factorial of the number 5 (five), 5!

# Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        
        # multiply result by i
        result *= i
    return result

# Calling the function 
n = 5

print(f"Factorial of {n} is {factorial(n)}")

# or Recursive lambda to calculate factorial
# factorial = (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1)) (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))

# n = 5
# print(f"Factorial of {n} is {factorial(n)}")
