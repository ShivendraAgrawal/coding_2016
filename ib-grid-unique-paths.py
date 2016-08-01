import math

def uniquePaths(A, B):
    total = A + B -2
    return math.factorial(total)/(math.factorial(A-1)*math.factorial(B-1))


A = 2
B = 2

print(uniquePaths(A, B))