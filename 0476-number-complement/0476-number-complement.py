class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num!=0:
            if num%2==0:
                binary+='1'
            else:
                binary +='0'
            num = num // 2
        #binary = binary[::-1]
        
        idx = 0
        ans = 0
        while idx<len(binary):
            ans += (int(binary[idx]) * (2**idx))
            idx +=1
        
        return ans