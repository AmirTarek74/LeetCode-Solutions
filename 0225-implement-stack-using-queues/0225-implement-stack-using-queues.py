class MyStack:

    def __init__(self):
        self.qu = collections.deque()

    def push(self, x: int) -> None:
        q = self.qu
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self.qu.popleft()

    def top(self) -> int:
        return self.qu[0]

    def empty(self) -> bool:
        return len(self.qu)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()