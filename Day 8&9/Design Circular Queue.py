class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0]*k
        self.rear = 0
        self.front = 0
        self.length = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1)%len(self.data)
        self.length += 1
        
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1)%len(self.data)
        self.length -= 1
        
        return True
        

    def Front(self) -> int:
        return self.data[self.front] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        return self.data[self.rear-1] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == len(self.data)
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()