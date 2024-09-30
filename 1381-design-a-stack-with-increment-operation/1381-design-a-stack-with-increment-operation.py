class CustomStack:

    def __init__(self, maxSize: int):
        self.capcity = maxSize
        self.size = 0
        self.stack = []
    def push(self, x: int) -> None:
        if self.size <self.capcity:
            self.stack.append(x)
            self.size += 1
            
    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -=1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        idx = 0
        if k<self.size:
            idx = k
        else:
            idx = self.size
        
        for i in range(idx):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)