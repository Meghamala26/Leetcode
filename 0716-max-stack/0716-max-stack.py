class MaxStack:

    def __init__(self):
        self.stack=[]
        self.heap=[]
        heapq.heapify(self.heap)
        self.removed=set()
        self.cnt=0
        
        

    def push(self, x: int) -> None:
        self.cnt+=1
        self.stack.append((x,self.cnt))
        heapq.heappush(self.heap,(-x,-self.cnt))
        

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
            
        last=self.stack.pop()
        self.removed.add(last[1])
        return last[0]
                       
                       
        
        
        

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
            
        return self.stack[-1][0]
        
        

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]
        
        

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        maxElem,idx= heapq.heappop(self.heap)
        self.removed.add(-idx)
        return -maxElem
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()