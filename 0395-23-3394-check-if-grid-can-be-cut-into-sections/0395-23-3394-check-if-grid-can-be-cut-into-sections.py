class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(rectangles, dim):
            res = 0
            rectangles.sort(key = lambda x:x[dim])

            maxi = rectangles[0][dim + 2]
            for i in range(1, len(rectangles)):
                rect = rectangles[i]
                if maxi <= rect[dim]:
                    res += 1
                maxi = max(maxi, rect[dim+2])
            
            return res >= 2
        
        return check(rectangles, 0) or check(rectangles, 1)