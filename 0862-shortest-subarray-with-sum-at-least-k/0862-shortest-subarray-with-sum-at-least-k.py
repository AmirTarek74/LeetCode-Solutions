class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
       
        n = len(nums)
        res = float("inf")
        summa = 0
        q = []
        heapq.heapify(q)
        for i in range(n):
            summa += nums[i]

            if summa>=k:
                res = min(res, i+1)

            while q and (summa - q[0][0])>=k:
                res = min(res, i - heapq.heappop(q)[1])

            heapq.heappush(q,[summa, i])


        return -1 if res == float("inf") else res