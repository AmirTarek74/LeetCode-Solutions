class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = 0
        trips = sorted(trips, key= lambda x:x[1])
        current_capacity = capacity
        
        trip_idx = 0
        history = []
        
        while trip_idx<len(trips):
            
            i = 0
            while history and i<len(history):
                if history[i][1]==location:
                    current_capacity += history[i][0]
                    temp = history.pop(i)
                else:
                    i+=1
            
            while trips[trip_idx][1]==location :
                if current_capacity<trips[trip_idx][0]:
                    return False
                current_capacity -= trips[trip_idx][0]
                history.append((trips[trip_idx][0],trips[trip_idx][2]))
                
                trip_idx +=1
                if trip_idx == len(trips):
                    break
            
            location += 1
            
            
            
        
        return True