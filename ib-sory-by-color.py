def sortColors(A):
    i, j, k = 0, 0, 0
    for index, color in enumerate(A):
        if color == 0:
            i += 1
        if color == 1:
            j += 1
        if color == 2:
            k += 1
    for index in range(0,len(A)):
        if i > 0:
            A[index] = 0
            i -= 1
        elif j > 0:
            A[index] = 1
            j -= 1
        elif k > 0:
            A[index] = 2
            k -= 1

    return A



A = [0, 1, 2, 0, 1, 2,0]
print(sortColors(A))