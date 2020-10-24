# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n
    f = [0,1] + [0]*(n-1)
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def pisano(m):
    a = 0
    b = 1
    for i in range(m * m + 1):
        a, b = b, (a+b)%m
        if a == 0 and b == 1:
            return  i + 1

def get_fibonacci_huge(n, m):
    n = n % pisano(m)
    fib_huge = calc_fib(n) % m
    return fib_huge

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
