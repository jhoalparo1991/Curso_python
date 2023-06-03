import time
import sys

sys.setrecursionlimit(2000000)

def not_factorial(n):
    result = 1
    while(n > 1):
        result *= n
        n -= 1
    return result


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    
    value = 1000000
    # Recursive function
    start = time.time()
    factorial(value)
    end = time.time()
    print(end - start)
    
    # Not recursive function
    start = time.time()
    not_factorial(value)
    end = time.time()
    print(end - start)

