class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        seen = set()
        q = initialBoxes
        has_used = [False] * len(status)
        while q:
            box = q.pop(0)
            has_used[box] = True
            if box in seen or status[box]==0:
                continue
            
            res += candies[box]
            seen.add(box)
            for contain in containedBoxes[box]:
                q.append(contain)
            for key in keys[box]:
                if has_used[key]:
                    q.append(key)
                status[key] = 1
        return res
            