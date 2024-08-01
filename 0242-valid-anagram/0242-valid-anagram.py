class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        else:
            d={}
            d2={}
            for c in s:
                if(c not in d.keys()):
                    d[c]=1
                else:
                    d[c]+=1
            for c in t:
                if(c not in d2.keys()):
                    d2[c]=1
                else:
                    d2[c]+=1
            for c in t:
                if c not in d.keys():
                    return False
                elif (d[c]!=d2[c]):
                    return False
        return True
        