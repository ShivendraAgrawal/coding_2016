class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        reverse_result = []
        len_a = len(A)
        i = len_a - 1
        carry = True
        while(i >= 0):
            digit = A[i]
            if carry:
                if digit + 1 > 9:
                    reverse_result.append(digit + 1 - 10)
                    carry = True
                else:
                    reverse_result.append(digit + 1)
                    carry = False
            else:
                reverse_result.append(digit)
            i -= 1
        if carry:
            reverse_result.append(1)
            carry = False

        while(reverse_result[-1] == 0):
            reverse_result.pop()

        return list(reversed(reverse_result))



A = [0,0,9,9,9]
s = Solution()
print(s.plusOne(A))