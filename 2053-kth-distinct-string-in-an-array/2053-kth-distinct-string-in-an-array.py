class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        out = []
        for i in range(len(arr)):
            if arr.count(arr[i])==1:
                out.append(arr[i])
        
        if len(out)==0 or k>len(out):
            return ""
        else:
            return out[k-1]
        