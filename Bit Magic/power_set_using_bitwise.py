s = "abc"
n = len(s)

power_size = 1 << n # to get power of 2

for i in range (power_size):
    for j in range(n): # char size is n
        if  (i & (1 << j) != 0):
            print(s[j], end="")
    print()
    