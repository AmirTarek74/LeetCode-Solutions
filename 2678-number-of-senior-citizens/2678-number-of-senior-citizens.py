class Solution:
    def countSeniors(self, details: List[str]) -> int:
        numberSeniors = 0
        for person in details:
            if int(person[11:13])>60:
                numberSeniors+=1
        
        return numberSeniors