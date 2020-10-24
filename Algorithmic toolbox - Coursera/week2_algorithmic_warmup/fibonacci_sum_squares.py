# Uses python3
from sys import stdin

def fib(n): 
    if n == 0: 
        return 0
    if n == 1 or n == 2: 
        return 1
  
    if f[n]: 
        return f[n] 
  
    if n & 1: 
        k = (n + 1) // 2
    else: 
        k = n // 2
        
    if n & 1: 
        f[n] = (fib(k) * fib(k) + 
                fib(k - 1) * fib(k - 1)) 
    else: 
        f[n] = ((2 * fib(k - 1) +
                     fib(k)) * fib(k)) 
    return f[n] 
  
def fibonacci_sum_squares(n): 
    n = n % 3660
    return (fib(n) * fib(n + 1))%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
