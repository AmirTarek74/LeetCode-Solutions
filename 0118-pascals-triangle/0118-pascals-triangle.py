class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        out = []
        lst = [1]
        out.append(lst)
        for row in range(2,numRows+1):
            lst = [1]
            idx = 1
            temp = out[row-2]
            while(len(lst)!=row-1):
                lst.append(temp[idx]+temp[idx-1])
                idx+=1
            lst.append(1)
            out.append(lst)
        return out
                
        