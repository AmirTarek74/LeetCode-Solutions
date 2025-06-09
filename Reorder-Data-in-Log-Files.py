class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        heap = []
        i = 1
        for log in logs:
            lst = log.split(" ")
            idt = lst[0]
            temp = " ".join([word for word in lst[1:]])
            if lst[1][0].isdigit():
                heapq.heappush(heap, (i, temp, idt))
                i += 1
            else:
                heapq.heappush(heap, (0, temp, idt))
        res = []
        while heap:
            _, log, idt = heapq.heappop(heap)
            res.append(idt+" "+log)
        
        return res