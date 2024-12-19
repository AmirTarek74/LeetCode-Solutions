class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for i in range(len(arr)):
            
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                max_num = stack[-1]
                while stack and arr[i]  < stack[-1]:
                    stack.pop()
                stack.append(max_num)
        
        return len(stack)
        