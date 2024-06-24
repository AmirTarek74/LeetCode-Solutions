class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [(difficulty[i],profit[i]) for i in range(len(difficulty))]
        job_profile.sort()
        worker.sort()
        maxprofit = 0
        profit = 0
        idx = 0
        for ability in worker:
            while idx < len(difficulty) and ability >= job_profile[idx][0]:
                maxprofit = max(maxprofit,job_profile[idx][1])
                idx+=1
            profit += maxprofit
        
        return profit

        