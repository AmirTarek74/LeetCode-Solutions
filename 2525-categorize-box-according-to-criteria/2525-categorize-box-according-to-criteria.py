class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_Bulky = False
        is_Heavy = False
        vol = length*width*height
        if length>= 10**4 or width>= 10**4 or height>= 10**4 or mass>= 10**4 or vol>=10**9 :
            is_Bulky = True
        if mass>=100:
            is_Heavy = True
        
        if is_Heavy and is_Bulky:
            return "Both"
        elif not is_Bulky and not is_Heavy:
            return "Neither"
        elif is_Heavy:
            return "Heavy"
        elif is_Bulky:
            return "Bulky"
            
        