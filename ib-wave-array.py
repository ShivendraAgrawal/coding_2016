class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i, ele in enumerate(A):
            if i%2 == 1:
                swap = A[i-1]
                A[i-1] = A[i]
                A[i] = swap
        return A

A = [1, 2, 3, 4]
print(len(A))
print(sorted(A))
s = Solution()
print(s.wave(A))