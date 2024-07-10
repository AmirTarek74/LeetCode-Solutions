class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = []
        for log in logs:
            if log=="../" :
                if len(steps)!=0:
                    item = steps.pop(len(steps)-1)
            elif log=='./':
                continue
            else:
                steps.append(log)
        return len(steps)
        