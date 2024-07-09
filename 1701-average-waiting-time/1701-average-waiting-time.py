class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        curr = -1
        for customer in customers:
            if customer[0]>= curr:
                time += customer[1]
                curr = customer[0]+customer[1]
            else:
                time = time + customer[1] + curr - customer[0]
                curr = curr + customer[1]
        return time/len(customers)

        