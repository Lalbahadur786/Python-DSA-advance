def max_even_odd_subarray(arr, n):
    res = 1
    curr = 1

    for i in range (1, n):
        if ((arr[i] % 2 == 0) and (arr[i-1] % 2 != 0)) or ((arr[i] % 2 != 0) and (arr[i-1] % 2 == 0)):
            curr += 1
            print(f"curr: {curr}, arr[{i}]: {arr[i]}")
            res = max(curr, res)
        else:
            curr = 1
    return res

arr = [0, 5, 4, 3, 4, 7, 10, 9]
n = len(arr)

print(max_even_odd_subarray(arr, n))
