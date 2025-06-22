class Stack:
    def __init__(self, cap):
        self.capacity = cap
        self.st = [None] * cap
        self.st_size = 0
        self.ax_arr = [None] * cap
        self.top = -1
        self.ax_top = -1

    def push(self, x):
        # Check if stack is full
        if self.st_size < self.capacity:
            # push elem into stack
            self.top += 1
            self.st[self.top] = x
            self.st_size += 1
            # if first elem then push into auxilary array
            if self.top == 0:
                self.ax_top += 1
                self.ax_arr[self.ax_top] = x
            elif self.st[self.top] <= self.ax_arr[self.ax_top]:
                self.ax_top += 1
                self.ax_arr[self.ax_top] = x
        else:
            return f"Stack is full. Cannot push {x}"
    
    def pop(self):
        # Check if stack is empty
        if self.top != -1:
            # popping the item
            num = self.st[self.top]
            self.st[self.top] = None
            self.top -= 1
            if num == self.ax_arr[self.ax_top]:
                self.ax_arr[self.ax_top] = None
                self.ax_top -= 1
            return num
        else:
            return "Stack is empty. Cannot pop item"

    def get_min(self):
        if self.ax_top == -1:
            return "Auxilary stack is empty"
        return self.ax_arr[self.ax_top]

stack = Stack(7)
stack.push(10)
stack.push(5)
print(f"pushed item: {stack.st}")
print(f"get_min: {stack.get_min()}")
print(f"pop: {stack.pop()}")
print(f"stack item: {stack.st}")
print(f"get_min: {stack.get_min()}")
print(f"pop: {stack.pop()}")
print(f"get_min: {stack.get_min()}")