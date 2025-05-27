# find unique numbers in list a, b

def intersect_of_two_arr(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    a_set = set()
    res = 0
    # first create set for arr1
    for i in range(m):
        a_set.add(arr1[i])

    for j in range(n):
        if arr2[j] in a_set:
            res += 1
            a_set.remove(arr2[j])
    return res

arr1 = [10, 15, 78, 98, 10]
arr2 = [10, 15, 87, 95, 36]
print(intersect_of_two_arr(arr1, arr2))
