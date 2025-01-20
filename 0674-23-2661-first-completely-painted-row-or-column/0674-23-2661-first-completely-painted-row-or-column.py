class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hashMap = {}
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            for c in range(cols):
                hashMap[mat[r][c]] = (r, c)
        
        rows_arr = [cols] * rows
        cols_arr = [rows] * cols

        for i in range(len(arr)):
            r, c = hashMap[arr[i]]
            rows_arr[r] -= 1
            cols_arr[c] -= 1
            if rows_arr[r] == 0 or cols_arr[c] == 0:
                return i
        
        return len(arr)
            