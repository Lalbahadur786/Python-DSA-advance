def print_groups(arr, n):
    # Given a binary list
    # need to flip only elem in2nd group of 0 and 1's

    for i in range(1, n):
        if arr[i] != arr[i-1]:
            if arr[i] != arr[0]:
                print("from", i, "to", end=" ")
            else:
                print(i - 1)
    if arr[n-1] != arr[0]:
        print(n - 1)

arr = [0, 0, 1, 1, 0, 0, 0, 1]
n = len(arr)
print_groups(arr, n)