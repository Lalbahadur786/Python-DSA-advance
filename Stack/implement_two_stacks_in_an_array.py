class two_stacks:
    def __init__(self, cap):
        self.size = cap
        self.arr = [None] * self.size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        # check if stack is full
        if self.top1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = x
            return True
        return False
    
    def push2(self, x):
        # check if stack is full
        if self.top1 < self.top2:
            self.top2 -= 1
            self.arr[self.top2] = x
            return True
        return False
    
    def pop1(self):
        if self.top1 > -1:
            num = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return num
        return -1
    
    def pop2(self):
        if self.top2 < self.size:
            num = self.arr[self.top2]
            self.arr[self.top2] = None  # Extras
            self.top2 += 1
            return num
        return -1
    
    def get_size1(self):
        return self.top1 + 1
    def get_size2(self):
        return self.size - self.top2 


two_stack_ob = two_stacks(7)
two_stack_ob.push1(10)
two_stack_ob.push2(30)
print(two_stack_ob.arr)
print(two_stack_ob.get_size1())
print(two_stack_ob.get_size2())
two_stack_ob.pop1()
two_stack_ob.pop2()
print(two_stack_ob.arr)
print(two_stack_ob.get_size1())
print(two_stack_ob.get_size2())