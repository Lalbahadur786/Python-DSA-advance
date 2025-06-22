class KStacks:
    def __init__(self, n, k):
        self.size = n
        self.arr = [None] * n
        self.top = [-1] * n
        self.free_top = 0
        self.next = [i+1 for i in range(n)]
        self.next[n - 1] = -1
    
    def push(self, sn, x):
        i = self.free_top
        self.free_top = self.next[self.free_top]
        self.arr[i] = x
        self.next[i] = self.top[sn]
        self.top[sn] = i
    
    def pop(self, sn):
        prev_top = self.top[sn]
        self.top[sn] = self.next[prev_top]
        self.next[prev_top] = self.free_top
        self.free_top = prev_top
        return self.arr[prev_top]
    
    def is_empty(self, sn):
        return self.top[sn] == -1


k_stack = KStacks(10, 3)
k_stack.push(0, 10)
k_stack.push(0, 20)
k_stack.push(1, 30)
print(k_stack.arr)
for i in range(3):
    print(f"{i}th top: {k_stack.top[i]}")