""" More than n by k occurance using moore's voting algo"""

def moore_ndk(arr, k):
    """
    """
    if k < 2:
        return
    
    temp = [[0 for i in range(2)]
            for i in range(k)]
    
    for i in range(k - 1):
        temp[i][0] = 0
    
    for i in range(len(arr)):
        j = 0
        while j < k - 1:
            if (temp[j][1] == arr[i]):
                temp[j][0] += 1
                break
            j += 1
        if j == k - 1:
            l = 0
            while l < k - 1:
                if (temp[l][0] == 0):
                    temp[l][1] = arr[i]
                    temp[l][0] = 1
                    break
                l += 1
            
            if l == k -1:
                while l < k:
                    temp[l][0] -= 1
                    l += 1
    
    for i in range(k - 1):
        ac = 0
        for j in range(len(arr)):
            if arr[j] == temp[i][1]:
                ac += 1
        
        if ac > len(arr) // k:
            print(f"Number: {temp[i][1]}, Count: {ac}")

arr1 = [4, 5, 6, 7, 8, 4, 4]
k = 3
moore_ndk(arr1, k)