class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        res = []
        while num:
            res.append(num%10)
            num = num // 10
        return res[::-1]