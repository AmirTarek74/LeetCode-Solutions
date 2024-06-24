class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num>9):
            sum=0
            num2 = str(num)
            for i in num2:
                sum+= int(i)
            num = sum
        
        return num
        