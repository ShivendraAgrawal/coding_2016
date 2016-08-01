def min_students(A, n):
    count = 0
    sum = 0
    for i in reversed(A):
        if i > n:
            return -1
        temp = sum + i
        if temp > n:
            sum = i
            count += 1
        else:
            sum += i
    return count + 1


def reqPainters(A, mid):
    total = 0
    numPainters = 1
    for i in range(len(A)):
        total += A[i]
        if (total > mid):
            total = A[i]
            numPainters += 1
    return numPainters

def binary_search(A, B, start, end):
    len_A = len(A)
    mid = (start + end)//2
    right = mid + 1
    left = mid - 1

    if start >= end:
        return start

    num_min_students = reqPainters(A, mid)
    # if num_min_students == -1:
    #     return binary_search(A, B, mid + 1, end)
    # if num_min_students == 0:
    #     return -1

    print(B, num_min_students)
    if B <= num_min_students:
        print(start, end, num_min_students, 'min', mid, B)
        right_result =  binary_search(A, B, right, end)
        if right_result != -1:
            return right_result
    if B == num_min_students:
        print(start, end, num_min_students, 'equal', mid, B)
        return mid
    if B >= num_min_students:
        print(start, end, num_min_students, 'max', mid, B)
        return binary_search(A, B, start, left)



def books(A, B):
    if B > len(A):
        return -1
    if B == len(A):
        return max(A)
    summation = 0
    for i in A:
        summation += i

    return binary_search(A, B, 0, summation)


# def books_ib(A, B):
#         lo = max(A)
#         hi = sum(A)
#         n = len(A)
#
#         if B > n:
#             return -1
#
#         while lo < hi:
#             mid = lo+(hi-lo)/2
#
#             requiredPainters = min_students(A, mid)
#             print(lo,mid,hi, requiredPainters)
#
#             if requiredPainters <= B:
#                 hi = mid
#             else:
#                 lo = mid + 1
#
#         return lo

A = [12, 34, 67, 90]
B = 2
# A = [ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ]
# B = 26

print(books(A, B))

# print(books_ib(A, B))

print(min_students(A,152))
# print(max_students(A,97))
print(reqPainters(A,152))
