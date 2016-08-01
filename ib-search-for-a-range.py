def binary_search_range(A, B, start, end, direction_left):
    len_A = len(A)
    mid = (start + end)//2
    right = mid + 1
    left = mid - 1

    if start > end:
        return -1
    if B == A[mid]:
        if direction_left:
            left_index = binary_search_range(A, B, start, left, True)
            if left_index != -1:
                return left_index
        else:
            right_index = binary_search_range(A, B, right, end, False)
            if right_index != -1:
                return right_index
        return mid
    if B >= A[mid]:
        return binary_search_range(A, B, right, end, direction_left)
    if B <= A[mid]:
        return binary_search_range(A, B, start, left, direction_left)

def searchRange(A, B):
    left_index = binary_search_range(A,B,0,len(A)-1,True)
    right_index = binary_search_range(A,B,0,len(A)-1,False)
    return [left_index, right_index]




A = [5, 7, 8, 8, 8, 10]
B = 5

print(searchRange(A,B))