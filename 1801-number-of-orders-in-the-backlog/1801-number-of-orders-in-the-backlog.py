class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 10**9 + 7
        sell, buy = [],[]
        
        for p,a,t in orders:
            if t==0:
                heapq.heappush(buy,[-p,a])
            else:
                heapq.heappush(sell,[p,a])
                
            while sell and buy and sell[0][0]<= -1 * buy[0][0]:
                k = min(sell[0][1],buy[0][1])
                sell[0][1] -= k
                buy[0][1] -= k
                if sell[0][1]==0:
                    heapq.heappop(sell)
                
                if buy[0][1]==0:
                    heapq.heappop(buy)
        
        return sum(a for p,a in sell+buy)%mod
        