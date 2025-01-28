def find_one_odd_occur(lst):
    res = 0
    for i in lst:
        res = res ^ i
    return res


lst = [4, 4, 4, 4, 1]
print(find_one_odd_occur(lst))