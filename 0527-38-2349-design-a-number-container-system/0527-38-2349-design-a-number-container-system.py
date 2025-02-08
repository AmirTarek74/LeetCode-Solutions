class NumberContainers:

    def __init__(self):
        self.idx = {}
        self.number = collections.defaultdict(SortedSet)
    def change(self, index: int, number: int) -> None:

        if index in self.idx:
            prev_num = self.idx[index]
            self.number[prev_num].remove(index)
            if not self.number[prev_num]:
                del self.number[prev_num]
        self.idx[index] = number
        self.number[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number:
            return -1
        return self.number[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)