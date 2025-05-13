class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        freq = [0] * 26

        for c in s:
            freq[ord(c)-ord("a")] += 1
        temp = [0] * 26
        for i in range(t):
            temp = [0] * 26
            for j in range(25):
                if freq[j] >0 :
                    temp[j+1] +=  freq[j]
            if freq[-1] >0 :
                temp[0] += freq[-1] 
                temp[1] += freq[-1]
            freq = temp
        return sum(freq)% mod          