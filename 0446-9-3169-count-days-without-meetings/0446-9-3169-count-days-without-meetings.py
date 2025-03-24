class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        start = meetings[0][0]
        end = meetings[0][1]
        res = start - 1
        for i in range(1, len(meetings)):
            new_s, new_end = meetings[i]
            if end > new_s or new_s == end:
                end = max(end, new_end)
            elif new_s > end:
                res = res + new_s - end - 1
                start = new_s
                end = new_end
        res += days - end
        return res