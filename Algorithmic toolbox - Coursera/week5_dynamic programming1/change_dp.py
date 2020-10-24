# Uses python3
import sys

def get_change(m):
    #write your code here
    minCoins = [0] + [1]*(m)
    for i in range(1,m+1):
        if i >= 4:
            minCoins[i] = min(minCoins[i-1], minCoins[i-3], minCoins[i-4]) + 1
        elif i >= 3:
            minCoins[i] = min(minCoins[i-1], minCoins[i - 3]) + 1
        else:
            minCoins[i] = minCoins[i-1] + 1
    return minCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
