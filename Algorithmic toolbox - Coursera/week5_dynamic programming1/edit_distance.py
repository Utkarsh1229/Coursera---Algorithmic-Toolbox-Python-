# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    
    row = len(t)
    col = len(s)
    
    D = np.asarray([[0]*(row+1)]*(col+1))
    
    for i in range(col+1):
        D[i][0] = i
        
    for i in range(row+1):
        D[0][i] = i
        
    for j in range(1, row+1):
        for i in range(1, col+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1]  + 1
            if s[i-1] == t[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
                
    return D[col][row]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
