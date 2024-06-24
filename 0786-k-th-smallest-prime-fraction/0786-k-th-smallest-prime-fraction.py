class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lst = []
        d = {}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                
                #if float(i/j) not in lst:
                lst.append(arr[i]/arr[j])
                d[arr[i]/arr[j]]=[arr[i],arr[j]]
        lst.sort(reverse=False)
        return d[lst[k-1]]