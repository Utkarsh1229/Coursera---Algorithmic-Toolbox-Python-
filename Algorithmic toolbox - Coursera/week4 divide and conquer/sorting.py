# Uses python3
import sys
import random


def partition3(a, l, r):
    #write your code here
    x = a[l]
    first = l
    last = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[i],a[first] = a[first],a[i]
            first+=1
            last+=1
            a[i],a[last] = a[last],a[i]
        elif a[i] == x:
            last+=1
            a[i],a[last] = a[last],a[i]
    return first,last

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m-1);
    randomized_quick_sort(a, n+1, r);
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
