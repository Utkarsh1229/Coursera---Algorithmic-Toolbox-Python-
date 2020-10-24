# Uses python3
import sys

def get_change(m):
    #write your code here
    coins_10 = m // 10
    rem1 = m % 10
    coins_5 = rem1 // 5
    coins_1 = rem1 % 5
    m = coins_10 + coins_5 + coins_1
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
