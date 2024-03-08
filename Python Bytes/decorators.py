import time

def measure_time(func):
    """ Explanation:
We define a decorator function called measure_time that takes a function func as an argument.
Inside the measure_time decorator, we define a wrapper function called wrapper that takes any positional arguments (*args) and keyword arguments (**kwargs) that will be passed to the original function.
Inside the wrapper function, we record the start time using time.time() before executing the original function func with the provided arguments using func(*args, **kwargs). The result of the function is stored in the result variable.
After the function execution, we record the end time using time.time() and calculate the execution time by subtracting the start time from the end time.
We print the execution time along with the name of the function using func.__name__.
Finally, we return the result of the original function.
We define a function called fibonacci that calculates the Fibonacci number for a given input n using recursion.
We decorate the fibonacci function with the @measure_time decorator, which automatically wraps the function with the time measurement functionality.
We call the fibonacci function with an argument of 30 and print the result.
When we run this code, it will calculate the 30th Fibonacci number and print the execution time of the fibonacci function. """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.5f} seconds")
        return result
    return wrapper

@measure_time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(2))