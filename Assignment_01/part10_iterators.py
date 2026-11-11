"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
# Warm-up:

def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print(number)
def evens(limit):
    for number in range(0, limit + 1, 2):
        yield number
print(list(evens(10)))

# Build:
with open("logs.txt", "w") as file:
    for i in range(1, 51):
        if i % 5 == 0:
            file.write(f"ERROR: Problem at line {i}\n")
        else:
            file.write(f"INFO: Normal operation {i}\n")
def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line
def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line
count = 0
for error in only_errors(read_lines("logs.txt")):
    count += 1
print("Total errors:", count)

# Challenge:

import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper
@timer
@log_calls
def calculate_sum(n):
    return sum(range(1, n + 1))
answer = calculate_sum(1000000)
print("Sum:", answer)

