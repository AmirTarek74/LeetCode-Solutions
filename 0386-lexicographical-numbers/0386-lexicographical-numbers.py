class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        
        for start in range(1,10):
            self.generate_numbers(start,n,res)
        
        return res
    
    
    def generate_numbers(self,curr,limit,res):
        
        if curr>limit:
            return
        
        res.append(curr)
        
        for next_digit in range(10):
            next_number = curr * 10 + next_digit
            
            if next_number <=limit:
                 self.generate_numbers(next_number,limit,res)
            else:
                break
    