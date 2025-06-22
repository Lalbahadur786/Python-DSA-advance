class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def push(self, x):
        self.top += 1
        self.arr.append(x)
    
    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.arr.pop()
        return "$"
    
    def is_operand(self, char):
        return char.isdigit()
    
    def evaluate_postfix(self, exp):
        for char in exp:
            # check if it is alpha
            if self.is_operand(char):
                self.push(char)
            else:
                # it is operator
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b + char + a)))
        print(self.arr.pop())

stack_ob = Stack()
stack_ob.evaluate_postfix("231*+9-")