class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num>0:
            binary += str(num%2)
            num = num // 2
        #binary = binary[::-1]
        comp = ''
        for i in range(len(binary)):
            if binary[i]=='0':
                comp += '1'
            else:
                comp += '0'
        
        #comp = comp[::-1]
        
        ans = 0
        for idx in range(len(comp)):
            ans += (int(comp[idx]) * (2**idx))
        
        return ans