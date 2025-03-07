class Solution:

    def isPrime(self, number):
        if number < 2:
            return False
        if number ==2 or number == 3:
            return True
        if number % 2 == 0:
            return False
        dom = 3
        while dom * dom <= number:
            if number % dom == 0:
                return False
            dom += 2
        
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prevPrime = -1
        close1 = -1
        close2 = -1
        mini = float("inf")

        for number in range(left, right + 1):
            if self.isPrime(number):
                if prevPrime != -1 : 
                    diff = number - prevPrime
                    if diff < mini:
                        mini = diff
                        close1 = prevPrime
                        close2 = number
                    if diff == 1 or diff == 2:
                        return [close1, close2]
                prevPrime = number
        
        return [close1, close2] if close1 != -1 else [-1 , -1]
        