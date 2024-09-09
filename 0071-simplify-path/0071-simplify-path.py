class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        q = []
        res = ''
        l = len(path)
        i = 0
        while i<l:
            if path[i]=='/':
                i+=1
                continue
            
            temp = ''
            while i<l and path[i]!='/':
                temp += path[i]
                i+=1
            
            if temp=='.':
                continue
            elif temp =='..':
                if q:
                    q.pop()
            else:
                q.append(temp)
        
        while q:
            res = '/' + q.pop() + res
        if len(res)==0:
            return '/'
        return res
            