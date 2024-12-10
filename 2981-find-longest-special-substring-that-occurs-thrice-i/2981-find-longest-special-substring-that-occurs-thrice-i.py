class Solution:
    def maximumLength(self, s: str) -> int:
        count =  {}
        
        for l in range(len(s)):
            cur_s = []
            for r in range(l, len(s)):
                if not cur_s or cur_s[-1]==s[r]:
                    cur_s.append(s[r])
                    cur_to_s = "".join(cur_s)
                    
                    count[cur_to_s] = count.get(cur_to_s, 0) + 1
                else:
                    break
        
        res = -1
        for s, freq in count.items():
            if freq>=3:
                res= max(res, len(s))
        
        return res
                    
               
       
