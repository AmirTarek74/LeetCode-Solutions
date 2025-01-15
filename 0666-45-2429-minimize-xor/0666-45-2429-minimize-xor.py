class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = 0
        target_set_bit = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31

        while set_bits_count < target_set_bit:
            if self.is_set(num1, current_bit) or (target_set_bit -set_bits_count > current_bit ):
                res = self.set_bit(res, current_bit)
                set_bits_count += 1
            current_bit -= 1
        
        return res
    

    def set_bit(self, x, bit):
        return x | (1<<bit)
    
    def is_set(self, x, current_bit):
        return (x & (1<<current_bit)) != 0 
        