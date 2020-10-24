# Uses python3
import sys



def fib_sum_last_digit(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    if a == 0:
        return 9
    else:
        return a - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_last_digit(n))
