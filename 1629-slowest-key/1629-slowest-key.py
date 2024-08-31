class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        pair = []
        pair.append((releaseTimes[0],keysPressed[0]))
        
        for i in range(1,len(releaseTimes)):
            pair.append((releaseTimes[i]-releaseTimes[i-1],keysPressed[i]))
        
        pair.sort(key=lambda x: (x[0],x[1]), reverse=True)
        
        return pair[0][1]