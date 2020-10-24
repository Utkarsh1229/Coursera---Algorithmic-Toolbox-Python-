# Uses python3
import math
import numpy as np

def evalt(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(M, m, i, j, operators):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, int(a), int(b),int(c), int(d))
        max_value = max(max_value, int(a), int(b), int(c), int(d))
    return min_value, max_value


def get_maximum_value(dataset):
    #write your code here
    operators, operands = [], []
    for i in dataset:
        if i in ['+','*','-']:
            operators.append(i)
        else:
            operands.append(i)
    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)

    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
