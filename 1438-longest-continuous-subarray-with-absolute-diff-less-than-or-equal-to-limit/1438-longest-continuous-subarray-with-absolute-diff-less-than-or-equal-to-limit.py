class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lst = []
        max_length = -1
        lst_max = nums[0]
        lst_min = nums[0]
        for num in nums:
            if lst_max < num:
                lst_max = num
            if lst_min > num:
                lst_min = num
            lst.append(num)
            if abs(lst_max - lst_min)>limit:
                temp = lst.pop(0)
                lst_max = max(lst)
                lst_min = min(lst)
            else:
                if len(lst)>max_length:
                    max_length = len(lst)
        return max_length            

        