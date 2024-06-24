class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        total =0 
        happiness.sort(reverse=True)
        for i in range(1,k+1):
            total += happiness[i-1]
            if i<len(happiness):
                if happiness[i]-i>0:
                    happiness[i] = happiness[i]-(i)
                else:
                    happiness[i] = 0
        
        return total
        