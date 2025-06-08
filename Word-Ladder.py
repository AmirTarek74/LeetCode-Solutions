class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        q = [beginWord]
        words = set(wordList)
        res = 1

        while q:
            n = len(q)

            for _ in range(n):
                word = q.pop(0)
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    for c in range(26):
                        temp_word = list(word)
                        temp_word[i] = chr(ord(\a\) + c)
                        temp_word = \\.join(temp_word)
                        if temp_word in words and temp_word not in seen:
                            seen.add(temp_word)
                            q.append(temp_word)
            res += 1
        return 0



