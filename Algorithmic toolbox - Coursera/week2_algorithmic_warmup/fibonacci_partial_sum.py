# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    else:
        a,b = 0,1
        for num in range((n-1)%60):
            rem = a + b
            rem = rem % 10
            b, a = rem, b
        return rem

def fib_sum_last_digit(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    if a == 0:
        return 9
    else:
        return a - 1

def fibonacci_partial_sum(from_, to):
    if (from_ == to):
        num = get_fibonacci_last_digit(from_)
        return num
    x = fib_sum_last_digit(from_ - 1)
    y = fib_sum_last_digit(to)
    if (y >= x):
        return (y-x)
    else:
        return ((y+10) - x)
 


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))