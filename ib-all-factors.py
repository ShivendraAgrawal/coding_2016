class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        result = []
        stop = int((A**(0.5)) // 1) + 1
        print(stop)
        for i in range(1,stop):
            if A%i == 0:
                result.append(i)
                result.append(A//i)
        result = list(set(result))
        return sorted(result)

    def isPrime(self, A):
        if A == 1:
            return 0
        stop = int((A**(0.5)) // 1) + 1
        for i in range(2,stop):
            if A%i == 0:
                return 0
        return 1


A = 18
s = Solution()
print(s.isPrime(A))