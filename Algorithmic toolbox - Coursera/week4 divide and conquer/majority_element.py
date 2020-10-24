# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    while (left <= right):
        mid = (left + right)//2
        if (a[mid] == x):
            return mid
        elif (x < a[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return -1

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    a = sorted(a)
    d = {}
    for elem in a:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] = d[elem] + 1
    y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
    if (d[y[0]] > len(a)//2):
        return  1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
