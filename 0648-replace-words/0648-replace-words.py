class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wrodArray = sentence.split()
        dictSet = set(dictionary)

        def shortestRoot(word,dict_set):
            for i in range(len(word)):
                prefix = word[0:i]
                if prefix in dict_set:
                    return prefix
            return word

        for word in range(len(wrodArray)):
            wrodArray[word] = shortestRoot(wrodArray[word],dictSet)

        return " ".join(wrodArray)
        