class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        m = float("inf")
        for i in range(1,len(arr)):
            prev = arr[i-1]
            curr = abs(arr[i]-prev)
            if curr<m:
                m = curr
                res = [[prev,arr[i]]]
            elif curr==m:
                res.append([prev,arr[i]])
        
        return res