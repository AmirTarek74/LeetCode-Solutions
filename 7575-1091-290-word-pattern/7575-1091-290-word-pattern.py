class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        mapping = {}
        word2char = {}
        for i in range(len(pattern)):
            if pattern[i] not in mapping and words[i] not in word2char :
                mapping[pattern[i]] = words[i]
                word2char[words[i]] = pattern[i]
            elif words[i] in word2char and word2char[words[i]] != pattern[i]:
                return False
            else:
                if mapping[pattern[i]] != words[i]:
                    return False
        
        return True

