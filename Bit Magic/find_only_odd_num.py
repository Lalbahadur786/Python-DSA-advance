lst = [10, 30, 10, 15, 10, 15, 10]

res = 0   # First will x ^ 0 = x
for num in lst:
    res = res ^ num  # think like you first xored even count nums
                     # You will zeros then 0^ odd occcur num = odd occur number

print(res)