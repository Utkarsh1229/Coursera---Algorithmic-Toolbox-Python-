# Uses python3
import sys
import math

def optimal_sequence(n):
    count = 0
    counts = [0,0] + [math.inf]*(n-1)
    
    for i in range(2, n+1):
        x, y = [math.inf]*2

        if i%3 == 0:
            x = counts[i//3] + 1
        if i%2 == 0:
            y = counts[i//2] + 1
        min_counts = min(x,y, counts[i-1] + 1)
        counts[i] = min_counts
        
    sequence = []
    sequence.append(n)
    
    while n!=1:
        if n%3 == 0 and counts[n] == counts[n//3] + 1:
            n = n//3
            sequence.append(n)
        elif n%2 ==0 and counts[n] == counts[n//2] + 1:
            n = n//2
            sequence.append(n)
        else:
            n = n - 1
            sequence.append(n)
            
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
