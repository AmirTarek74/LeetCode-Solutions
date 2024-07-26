class Solution:
    def countTime(self, time: str) -> int:
        answer = 1
        if time[3]=='?':
            answer *= 6
        
        if time[4]=='?':
            answer *= 10
        
        if time[0:2]=='??':
            answer *=24
        elif time[0]=='?' and time[1]!='?':
            answer *= 2 if time[1] in ['4','5','6','7','8','9'] else 3
        elif time[1]=='?':
            answer *= 10 if time[0] in ['0','1'] else 4
        
        return answer
        