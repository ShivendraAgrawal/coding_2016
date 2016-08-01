class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        flag = False
        len_a = len(A)
        if len_a < 2:
            return A
        for i in range(len_a-2, -1, -1):
            if A[i] < A[i+1]:
                flag = True

                A = A[:i+1] + sorted(A[i+1:])

                for j in range(i+1, len_a):
                    if A[j] > A[i]:
                        swap = A[i]
                        A[i] = A[j]
                        A[j] = swap
                        break

                break
        if flag:
            return A
        else:
            return sorted(A)


A = [1, 2, 5, -7, 2, 3]
A = [ 0, 0, -1, 0 ]
A = [ 3,4,2,1]
# A = [1,2,3]
# A= [3,2,1]
# A  = [1,1,5]
# A = [20, 50, 113]
# A = [3,5,4,2,1]
s = Solution()
print(s.nextPermutation(A))