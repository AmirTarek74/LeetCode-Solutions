class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array = []
        res = 0
        for row in grid:
            for num in row:
                array.append(num)
        
        array.sort()
        l = len(array)
        common = array[l//2]

        for number in array:
            if number % x != common%x:
                return -1
            
            res += abs(number - common)//x
        
        return res