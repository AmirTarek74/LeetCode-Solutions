class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
           
            for c in s:
                t1 = s.count(c)
                t2 = t.count(c)
                if t1!=t2:
                    return False
            return True
        