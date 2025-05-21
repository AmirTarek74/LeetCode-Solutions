class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i):
            if len(cur) == k:
                res.append(cur[:])
                return
            for num in range(i, n+1):
                cur.append(num)
                backtrack(num+1)
                cur.pop()
        backtrack(1)
        return res