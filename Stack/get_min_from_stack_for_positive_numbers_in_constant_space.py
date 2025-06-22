class Stack:
    def __init__(self, cap):
        self.capacity = cap
        self.st = [None] * cap
        self.size = 0
        self.top = -1
        self.min = -1
    
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    def is_full(self):
        if self.top == self.capacity - 1:
            return True
        return False
    
    def peek(self):
        if not self.is_empty():
            num = self.st[self.top]
            if num <= 0:
                return self.min
            else:
                return num
        else:
            return "Stack is empty. Cannot peek item"
    
    def push(self, x):
        # Check if cap is full
        if self.is_empty():
                # this means stack is not full
                self.top += 1
                self.st[self.top] = x
                self.min = x
        else:
            if not self.is_full():
                if x < self.min:
                    self.top += 1
                    self.st[self.top] = x - self.min
                    self.min = x
                else:
                    self.top += 1
                    self.st[self.top] = x
            else:
                return f"Stack is full. Cannot push {x}"
    
    def pop(self):
        # Check if stack is empty
        if not self.is_empty():
            num = self.st[self.top]
            self.top -= 1
            if num <= 0:
                num1 = self.min
                self.min = self.min - num
                return num1
            else:
                return num


        else:
            return "Stack is empty. Cannot pop item"

stack = Stack(7)
stack.push(5)
stack.push(10)
stack.push(2)
stack.push(6)
print(stack.st)
print(stack.min)
print(stack.peek())
