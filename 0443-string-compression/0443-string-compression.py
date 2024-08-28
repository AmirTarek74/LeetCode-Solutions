class Solution:
    def compress(self, chars: List[str]) -> int:
        
        res = 0
        i = 0
        while i<len(chars):
            cur_len = 1
            while (i+cur_len < len(chars) and chars[i+cur_len]==chars[i]):
                cur_len +=1
            chars[res] = chars[i]
            if cur_len==1:
                res += 1
                i+=1
            else:
                s = str(cur_len)
                chars[res+1:res+1+len(s)] = list(s)
                res +=  len(s) + 1
                i = i + cur_len
        
        return res
        