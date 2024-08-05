class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        pairs = [(h, name) for h,name in zip(heights, names)]
        pairs.sort(reverse=True)
        names = [name for _,name in pairs]
        return names
        