# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    proportion = []
    for i,j,k in zip(values, weights, range(n)):
        prop = i/j
        proportion .append([prop,k])
    #print (proportion)
    new_prop = sorted(proportion, key = lambda x:x[0], reverse = True)
    #print (new_prop)
    # write your code here
    for _ in new_prop:
        i = _[1]
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        value = value + a * (values[i]/ weights[i])
        weights[i] -= a
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
