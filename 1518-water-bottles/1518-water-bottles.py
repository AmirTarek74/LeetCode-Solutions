class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        drunk_water = 0
        drunk_water += numBottles
        while numBottles>=numExchange:
            drunk_water += numBottles//numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange
        
        return drunk_water
        