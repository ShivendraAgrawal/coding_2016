# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        j = 0
        intervals.sort(key=lambda x:x.start)
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            # print(intervals[i].start, intervals[i].end)
            if intervals[i].start <= result[j].end:
                # print(result[j].start, result[j].end)
                result[j].start = min(result[j].start, intervals[i].start)
                result[j].end = max(result[j].end, intervals[i].end)
                # print(result[j].start, result[j].end)
                # print
            else:
                j += 1
                result.append(Interval(intervals[i].start, intervals[i].end))

        return result


A = [[1,3],[2,6],[8,10],[15,18],[3,5]]
A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
A = [ (4, 100), (48, 94), (16, 21), (58, 71), (36, 53), (49, 68), (18, 42), (37, 90), (68, 75), (6, 57), (25, 78), (58, 79), (18, 29), (69, 94), (5, 31), (10, 87), (21, 35), (1, 32), (7, 24), (17, 85), (30, 95), (5, 63), (1, 17), (67, 100), (53, 55), (30, 63), (7, 76), (33, 51), (62, 68), (78, 83), (12, 24), (31, 73), (64, 74), (33, 40), (51, 63), (17, 31), (14, 29), (9, 15), (39, 70), (13, 67), (27, 100), (10, 71), (18, 47), (48, 79), (70, 73), (44, 59), (68, 78), (24, 67), (32, 70), (29, 94), (45, 90), (10, 76), (12, 28), (31, 78), (9, 44), (29, 83), (21, 35), (46, 93), (66, 83), (21, 72), (29, 37), (6, 11), (56, 87), (10, 26), (11, 12), (15, 88), (3, 13), (56, 70), (40, 73), (25, 62), (63, 73), (47, 74), (8, 36) ]
A = [ (54, 75), (56, 60), (61, 86), (22, 43), (56, 87), (32, 53), (14, 81), (64, 65), (9, 42), (12, 33), (22, 58), (84, 90), (27, 59), (41, 48), (43, 47), (22, 29), (16, 23), (41, 72), (15, 87), (20, 59), (45, 84), (14, 77), (72, 93), (20, 58), (47, 53), (25, 88), (5, 89), (34, 97), (14, 47) ]

intervals = []
for i in A:
    intervals.append(Interval(i[0],i[1]))
print(len(A))
print(sorted(A, key=lambda x:x[0]))
s = Solution()
for i in s.merge(intervals):
    print(i.start, i.end)