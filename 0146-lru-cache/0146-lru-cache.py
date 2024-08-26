class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in list(self.d.keys()):
            return -1
        val = self.d.pop(key)
        self.d[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in list(self.d.keys()):
            temp = self.d.pop(key)
        else:
            if len(self.d)==self.c:
                temp = self.d.pop(list(self.d.keys())[0])
        
        self.d[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)