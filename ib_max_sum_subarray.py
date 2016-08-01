class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = 0
        max_till_here = 0
        for i in A:
            max_till_here += i

            if max_till_here < 0:
                max_till_here = 0
            if max_so_far < max_till_here:
                max_so_far = max_till_here
        if max_so_far > 0:
            return max_so_far
        else:
            return max(A)

A = [-2,1,-3,4,-1,2,1,-5,4]
A = [-2, -3, -4, -1, -5, -6]

s = Solution()
print(s.maxSubArray(A))