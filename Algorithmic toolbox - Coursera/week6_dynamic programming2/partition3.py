# Uses python3
import sys
import itertools
import numpy as np

def partition3(A):
    if len(A)<3:
        return 0
    elif sum(A)%3 != 0:
        return 0
    else:
        W = sum(A)//3
        cnt = 0
        value = np.zeros((W+1, len(A) + 1))
        for i in range(1, W+1):
            for j in range(1, n+1):
                value[i][j] = value[i][j-1]
                if A[j-1] <= i:
                    val = value[i-A[j-1]][j-1] + A[j-1]
                    if val > value[i][j]:
                        value[i][j] = val
                if value[i][j] == W:
                    cnt += 1
        if cnt < 3:
            return 0
        else:
            return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

