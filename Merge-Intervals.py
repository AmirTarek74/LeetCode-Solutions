class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals:
            if interval[0]>end:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])
        res.append([start, end])
        return res