def mySort(x):
    x.sort()
    return x
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            d[word] = d.get(word,0) + 1
        d = {key: value for key,value in sorted(d.items(), key=lambda item:item[1],reverse=True)}
        keys = list(d.keys())
        values = list(d.values())
        i, j = 0, 0
        output = []
        while i != len(values) and j != len(values):
            if values[i]==values[j]:
                j+=1
            else:
                
                output = output + mySort(keys[i:j])
                i = j
        
        output = output + mySort(keys[i:j])
        return output[0:k]
            
        