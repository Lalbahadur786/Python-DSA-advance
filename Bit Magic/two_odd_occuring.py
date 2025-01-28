def two_odd_occur(lst):
    res1 = res2 = 0
    xors = 0
    # First find the one odd occur
    for i in lst:
        xors = xors ^ i
    
    # Now you have got  xor of two odds 5^6
    # now grouping is required
    sn = xors & ~(xors - 1) # last bit will be set as 1

    for i in lst:
        if i & sn != 0:
            # this means last bit is set
            res1 = res1 ^ i  # this will make a grouping where
                             # first odd num will present
        else:
            res2 = res2 ^ i  # Second group

    return res1, res2

lst = [3, 3, 4, 4, 5, 6]
print(two_odd_occur(lst))
