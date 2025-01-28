n = 14

def is_power_of_2(n):
    if n == 0:
        return False
    return (n & (n-1) == 0)

print(is_power_of_2(n))