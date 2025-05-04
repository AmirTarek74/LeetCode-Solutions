class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = {}

        res = 0

        for i, j in dominoes:
            pair = (min(i,j), max(i,j))
            counter[pair] = counter.get(pair,0) + 1

        for k in counter:
            if counter[k]>1:
                res += int(math.factorial(counter[k])/ (math.factorial(2)*math.factorial(counter[k]-2) ))
        return res 