class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        
    def push(self, value):
        self.data.append(value)
        self.top += 1
    
    def pop(self):
        val = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return val
    
    def peek(self):
        print(self.data[self.top])
    
    def print_stack(self):
        for value in self.data:
            print(value)
            
cstk = Stack()
cstk.push(5)
cstk.push(4)
print(cstk.pop())
cstk.peek()