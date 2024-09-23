class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        q = []
       
        
        p = set(positive_feedback)
        n = set(negative_feedback)
        res = []
        for idx,id in enumerate(student_id):
            score = 0
            for word in report[idx].split(' '):
                if word in p:
                    score +=3
                elif word in n:
                    score -=1
            
            q.append([-score,id])
        
        q.sort()
           
        
        
        return [student[1] for student in q[:k]]
                