class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        d2 = {key: value for key, value in sorted(d.items(), key= lambda x:x[1], reverse= True)}
        output = []
        for i in range(k):
            output.append(list(d2.keys())[i])
        
        return output
        