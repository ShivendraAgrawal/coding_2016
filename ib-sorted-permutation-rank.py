import math

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        char_array = [i for i in A]
        len_a = len(char_array)
        rank_map = {}
        rank = 0
        for i in sorted(char_array):
            rank_map[i] = rank
            rank += 1

        net_rank = 0
        for i, character in enumerate(char_array):
            for key in rank_map:
                if key > character:
                    rank_map[key] -= 1

            net_rank += rank_map[character] * math.factorial(len_a - 1 - i)

        return (net_rank + 1)% 1000003


A = 'acdb'
A = 'bacd'
s = Solution()
print(s.findRank(A))