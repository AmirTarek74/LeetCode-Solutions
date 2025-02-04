class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
       
        char = ord(coordinates[0]) - ord('a')
        num = int(coordinates[1])
      
        return (num + char)%2 == 0
        