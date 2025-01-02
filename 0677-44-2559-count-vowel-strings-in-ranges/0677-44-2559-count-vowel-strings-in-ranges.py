class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e','i','o','u']
        prefix = [0] * (len(words) + 1)

        for i in range(1, len(words)+1):
            
            if words[i-1][0] in vowels and words[i-1][-1] in vowels:
                prefix[i] += prefix[i-1] + 1 
            else:
                prefix[i] += prefix[i-1]
        
        res = []
        for i in range(len(queries)):
            s, e = queries[i]

            res.append(prefix[e+1]-prefix[s+1] + (1 if prefix[s]!=prefix[s+1] else 0))
        
        return res
        