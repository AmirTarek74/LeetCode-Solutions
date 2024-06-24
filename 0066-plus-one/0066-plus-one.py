class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        num = 0
        for i in range(l):
            num =  num*10+digits[i]
        num+=1
        lst = []
        while(num!=0):
            rem = num%10
            num = num/10
            lst.insert(0,rem)
        
        return lst

        