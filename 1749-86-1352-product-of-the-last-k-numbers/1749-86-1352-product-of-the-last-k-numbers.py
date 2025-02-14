class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        self.zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.zero = max(self.zero, len(self.stream))
            self.stream.append(1)
        else:
            self.stream.append(self.stream[-1]*num)

    def getProduct(self, k: int) -> int:
        if self.zero >= len(self.stream) - k:
            return 0
        else:
            res = self.stream[-1]//self.stream[-k-1]
            return res
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)