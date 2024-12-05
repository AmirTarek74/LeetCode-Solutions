class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sq = []
        tq = []
        
        for i in range(len(start)):
            if start[i] != '_':
                sq.append((start[i], i))
            
            if target[i] != '_':
                tq.append((target[i], i))
        
        if len(sq) != len(tq):
            return False
    
        
        while sq:
            start_c, start_idx = sq.pop(0)
            target_c, target_idx = tq.pop(0)
            
            if start_c != target_c or (start_c == 'L' and start_idx < target_idx) or (start_c == 'R' and start_idx > target_idx):
                return False
        
        return True