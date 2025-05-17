class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        aux = []
        for n in nums:
            if n == val:
                continue
            aux.append(n)
        for i in range(len(aux)):
            nums[i] = aux[i]
        return len(aux)