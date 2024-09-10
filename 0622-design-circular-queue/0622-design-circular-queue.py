class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [-1]*self.k
        self.front = -1
        self.rear = -1
        
    
    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.q[self.rear] = value
            return True
        elif self.isFull():
            return False
        else:
            self.rear  = (self.rear + 1)%self.k
            self.q[self.rear] = value
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
            
        else:
            self.front = (self.front+1)%self.k
           
        return True

    def Front(self) -> int:
        return self.q[self.front]

    def Rear(self) -> int:
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front==-1

    def isFull(self) -> bool:
        if self.front == self.rear+1:
            return True
        elif self.rear == self.k-1 and self.front ==0 :
            return True
        
        return self.rear == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()