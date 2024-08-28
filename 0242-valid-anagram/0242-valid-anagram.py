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
            d1 = {}
            d2 = {}
            for i in range(len(t)):
                d1[s[i]] = d1.get(s[i],0) + 1
                d2[t[i]] = d2.get(t[i],0) + 1
            for k in list(d1.keys()):
                if k not in list(d2.keys()):
                    return False
                elif d1[k]!=d2[k]:
                    return False
            return True
        