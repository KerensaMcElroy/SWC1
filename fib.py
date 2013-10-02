import doctest
import sys

def factorial(n):
    '''Returns the factorial of N
    
    F(N) = N!= N * (N-1) * (N-2)...*1
    F(0) = 1
    
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(10)
    3628800
    '''
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
    
def fibonacci(n):
    '''Returns the Nth value in the Fibonacci
    sequence
    
    F(N) = F(N-1) + F(N-2)
    F(0) = 0, F(1) = 1
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    '''
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

if __name__ == "__main__":    
    doctest.testmod()
