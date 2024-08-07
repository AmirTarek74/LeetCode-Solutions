class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while q and temperatures[i]>q[-1][0]:
                temp, temp_index = q.pop()
                result[temp_index] = i - temp_index
            
            q.append((temperatures[i],i))

        return result
                
        
       

        