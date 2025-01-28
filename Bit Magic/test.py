def check_bits(pattern, arr, N):
        count = 0
        for i in range(N):
            if (pattern & arr[i]) == pattern:
                print(f"pattern: {pattern}")
                print(f"a[i]: {arr[i]}")
                count += 1
        return count

def maxAND(arr,N):
        #Your code here
        
        res = 0
        
        for bit in range(31, -1, -1):
            count = check_bits(res | (1 << bit), arr, N)
            print(f"count = {count}")
            
            if count >= 2:
                res = res | (1 << bit)

                print(f"set res {res}")
            
        print(f"res: {res}")

arr = [4, 8 , 6 , 2]
N = len(arr)
maxAND(arr,N)