class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrck(curr,i,total):
            if total==target:
                res.append(curr[:])
                return
            if i>=len(candidates) or total>target:
                return
            curr.append(candidates[i])
            backtrck(curr,i+1,total+candidates[i])
            curr.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrck(curr,i+1,total)
            
        backtrck([],0,0)
        
        return res