" This is to time 2 functions"

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.5f} seconds")
        return result
    return wrapper

@measure_time
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

@measure_time
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

# Example usage
nums = [2, 7, 11, 15]
target = 9
result_two_sum = two_sum(nums, target)
print("Two Sum result:", result_two_sum)

s = "()[]{}"
result_valid_parentheses = is_valid_parentheses(s)
print("Valid Parentheses result:", result_valid_parentheses)