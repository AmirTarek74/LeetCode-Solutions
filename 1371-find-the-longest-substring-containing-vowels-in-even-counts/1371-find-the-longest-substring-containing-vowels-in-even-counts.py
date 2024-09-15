class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        prefix_Xor = 0
        ch_map = [0] * 26
        ch_map[ord('a')-ord('a')] = 1
        ch_map[ord('e')-ord('a')] = 2
        ch_map[ord('i')-ord('a')] = 4
        ch_map[ord('o')-ord('a')] = 8
        ch_map[ord('u')-ord('a')] = 16
        
        mp = [-1] * 32
        res = 0
        for i in range(len(s)):
            prefix_Xor ^= ch_map[ord(s[i]) - ord('a')]
            
            if mp[prefix_Xor] == -1 and prefix_Xor!=0:
                mp[prefix_Xor] = i
            res = max(res, i - mp[prefix_Xor])
        
        return res