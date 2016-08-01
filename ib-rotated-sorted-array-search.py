def helper_1(A, B, start, end):
    len_A = len(A)
    mid = (start + end)//2
    right = (mid + 1)%len_A
    left = (mid - 1 + len_A)%len_A
    # print(len_A, A[0],A[-1], left, mid, right)
    # print(A)
    # print
    if A[mid] == B:
        return mid
    
    if A[start] <= A[end]:
        if B > A[mid]:
            return helper_1(A, B, right, end)
        if B < A[mid]:
            return helper_1(A, B, start, left)
    if A[mid] <= A[right] and A[mid] <= A[left] and A[mid] == B:
        return mid
    if A[mid] > A[start]:
        if B > A[mid]:
            return helper_1(A, B, right, end)
        if B < A[mid]:
            return helper_1(A, B, start, left)
    if A[mid] < A[end]:
        if B > A[mid]:
            return helper_1(A, B, right, end)
        if B < A[mid]:
            return helper_1(A, B, start, left)

def helper(A, start, end):
    len_A = len(A)
    mid = (start + end)//2
    right = (mid + 1)%len_A
    left = (mid - 1 + len_A)%len_A

    if end - start == 1:
        if A[start] < A[end]:
            return start
        if A[start] > A[end]:
            return end
    if A[start] <= A[end]:
        return start
    if A[mid] <= A[right] and A[mid] <= A[left]:
        return mid
    if A[mid] > A[start]:
        return helper(A, right, end)
    if A[mid] < A[end]:
        return helper(A, start, left)

def binary_search(A, B, start, end):
    len_A = len(A)
    mid = (start + end)//2
    right = mid + 1
    left = mid - 1

    if B == A[mid]:
        return mid
    if start >= end:
        return -1
    if B > A[mid]:
        return binary_search(A, B, right, end)
    if B < A[mid]:
        return binary_search(A, B, start, left)


def search(A, B):
    min_index = helper(A, 0, len(A)-1)
    print(min_index)

    if A[min_index] == B:
        return min_index
    right_index = binary_search(A, B, min_index + 1, len(A)-1)
    left_index = binary_search(A, B, 0, min_index - 1)

    if right_index != -1:
        return right_index
    if left_index != -1:
        return left_index
    return -1


A = [4, 5, 6, 7, 0, 1, 2]
A = [ 9, 10, 12, 13, 24, 26, 27, 28, 29, 43, 48, 51, 54, 56, 57, 59, 62, 66, 70, 71, 72, 74, 75, 77, 78, 81, 83, 85, 87, 88, 89, 90, 91, 92, 93, 97, 98, 99, 101, 102, 104, 105, 107, 112, 113, 115, 123, 126, 127, 132, 133, 134, 135, 136, 143, 144, 148, 150, 151, 152, 154, 159, 160, 161, 163, 167, 169, 170, 174, 176, 177, 179, 180, 181, 183, 185, 186, 187, 188, 193, 194, 196, 197, 198, 199, 200, 203, 1, 6, 7, 8 ]

# A = [1,2,3,4,5,8,9]
B = 38
# print(binary_search(A, B, 0, len(A)-1))
print(search(A,B))