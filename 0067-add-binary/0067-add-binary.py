class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = 0
        for i in range(len(a)-1,-1,-1):
            num1+=int(a[i])*2**(len(a)-1-i)
        num2 = 0
        for i in range(len(b)-1,-1,-1):
            num2+=int(b[i])*2**(len(b)-1-i)
        out = num1+num2
        lst = []
        if out==0:
            return "0"
        while(out!=0):
            lst.insert(0,out%2)
            out/=2
        out2 = [str(i) for i in lst]
        out =''
        for c in out2:
            out+=c

        
        return out