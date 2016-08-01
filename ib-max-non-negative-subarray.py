class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_start = 0
        max_stop = 0
        start = max_start
        stop = max_stop

        max_so_far = 0
        max_till_here = 0
        length_so_far = 0
        length_till_here = 0
        flag = False
        for i,ele in enumerate(A):
            if ele >= 0:
                flag = True
                max_till_here += ele
                length_till_here += 1
                if max_till_here > max_so_far:
                    max_start = start
                    max_stop = i
                    max_so_far = max_till_here
                    length_so_far = length_till_here
                    # print('first  ',max_start,max_stop, max_so_far, length_so_far)
                if max_till_here == max_so_far and length_till_here > length_so_far:
                    max_start = start
                    max_stop = i
                    # print(max_start,max_stop)
                    length_so_far = length_till_here
            else:
                start = i+1
                # print(start)
                max_till_here = 0
                length_till_here = 0

        if not(flag):
            return []
        return A[max_start:max_stop+1]


A = [1, 2, 5, -7, 2, 3]
A = [ 0, 0, -1, 0 ]
A = [ 137806862, -982906996, -511702305, -1937477084 ]
s = Solution()
print(s.maxset(A))