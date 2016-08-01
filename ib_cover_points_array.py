class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def min_single_distance(self, x1,y1,x2,y2):
        return max(abs(x2-x1), abs(y2-y1))


    def coverPoints(self, X, Y):
        total_min = 0
        n = len(X)
        for i in range(n-1):
            total_min += self.min_single_distance(X[i],Y[i], X[i+1],Y[i+1])

        return total_min


X = [0,1,1]
Y = [0,1,2]
s = Solution()
print(s.coverPoints(X,Y))