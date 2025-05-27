# find unique numbers in list a, b

def union_of_two_arr(arr1, arr2):
    u_set = set()
    for elem in arr1+arr2:
        u_set.add(elem)
    return len(u_set)


arr1 = [10, 15, 78, 98, 10]
arr2 = [10, 15, 87, 95, 36]
print(union_of_two_arr(arr1, arr2))
