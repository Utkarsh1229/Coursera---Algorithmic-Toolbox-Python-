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

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
