def findCount(A, B):
    len_A = len(A)
    if len_A == 0:
        return 0

    mid = len_A // 2
    print(A, mid)
    if B < A[mid]:
        return findCount(A[:mid], B)
    elif B > A[mid]:
        return findCount(A[mid+1:], B)
    elif B == A[mid]:
        return findCount(A[:mid], B) + 1+ findCount(A[mid+1:], B)


A = (5, 7, 7, 8, 8, 10)
B = 8

print(findCount(A, B))