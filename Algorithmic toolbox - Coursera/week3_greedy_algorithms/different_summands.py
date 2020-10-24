# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if n == 1:
        summands.append(n)
        return summands
    sum_summands = 0
    for i in range(1,n):
        if(sum_summands >= n):
            break
        elem = check(n, i, sum_summands)
        summands.append(elem)
        sum_summands += elem
    
    return summands
def check(n, lower_bound, sum_summands):
    if (sum_summands + 2 * lower_bound + 1)>n:
        return n - sum_summands
    return lower_bound

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
