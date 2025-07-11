class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        res = ""
        stack = []
        minChar = 'a'

        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while minChar != 'z' and cnt[minChar] == 0:
                minChar = chr(ord(minChar) + 1)
            while stack and stack[-1] <= minChar:
                res += stack.pop()
        return res