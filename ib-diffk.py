def diffPossible(A, B):
    right_most = len(A)
    for i in range(len(A)-1, 0, -1):
        for j in range(0, right_most):
            if A[i] - A[j] < B:
                right_most = j
                break
            elif A[i] - A[j] == B and i != j:
                return True
    return False


A = [1, 3, 5]
A = [ 1, 2, 3 ]
B = 4
B = 0

print(diffPossible(A, B))
