# Uses python3
import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a,a)

def lcm(a, b):
    return (int(a*b/gcd(a,b)))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

