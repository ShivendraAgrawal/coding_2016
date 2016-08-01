def findIntersection(A, B):
    result = []
    len_A = len(A)
    len_B = len(B)
    i, j = 0, 0

    while(i < len_A and j < len_B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            result.append(A[i])
            i += 1
            j += 1

    return result


A = [1,2,3,4,5,5,6,9]
B = [3,5,5,6,7,8]

print(findIntersection(A, B))