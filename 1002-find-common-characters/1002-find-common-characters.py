class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        out = []

        for i in range(len(words)):
            
            for c in words[i]:
                counter = 0
                count = words[i].count(c)
                mini = count
                for j in range(i+1,len(words)):
                    if c in words[j] and c not in out:
                        counter+=1
                        if mini >= words[j].count(c):
                            mini = words[j].count(c)
                        
                if counter==(len(words)-1) :
                    for _ in range(mini):
                        out.append(c)
                
                
        return out
         