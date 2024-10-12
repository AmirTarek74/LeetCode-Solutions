class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for e in intervals:
            events.append([e[0],1])
            events.append([e[1]+1,-1])
        
        events.sort(key= lambda x:[x[0],x[1]])
        
        res = 0
        cur_sum = 0
        
        for event in events:
            cur_sum += event[1]
            
            res = max(res,cur_sum)
        
        return res