class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if tops == bottoms:
            return 0
        
        res = float("inf")

        for i in range(1,7):
            valid = True
            top = 0
            bottom = 0
            for t, b in zip(tops, bottoms):
                if i != t and i != b:
                    valid = False
                    break
                if i != t:
                    top += 1
                if b != i:
                    bottom += 1
            if valid:
                res = min(res, min(top, bottom))
        return res if res != float("inf") else -1