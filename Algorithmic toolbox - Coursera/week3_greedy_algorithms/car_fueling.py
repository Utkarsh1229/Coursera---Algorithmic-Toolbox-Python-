# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num_refills = 0
    curr_refill = 0
    n = len(stops)
    stops.insert(0,0)
    stops.append(distance)
    while stops[curr_refill] + tank < distance:
        lastRefill = curr_refill 
        while (curr_refill <= n - 1 and (stops[curr_refill + 1] - stops[lastRefill] <= tank)):
            curr_refill = curr_refill + 1
        if curr_refill == lastRefill:
            return -1
        if curr_refill <= n:
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
