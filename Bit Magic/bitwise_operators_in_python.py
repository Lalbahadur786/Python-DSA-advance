x = 5
y = 6

# Bitwise AND
print(x & y) # 4

# Bitwise OR
print(x | y) # 7

# Bitwise XOR
print(x^y) # 3

# How the NOT operator works
# it takes the binary representation of the number and inverts all the bits
# and then adds 1 to the result (2's complement representation)
# Bitwise NOT
print(~x) # -6

# Left Shift
print(x << 1) # 10
print(x << 2) # 20
print(x << 3) # 40

# Right Shift
print(x >> 1) # 2
print(x >> 2) # 1
print(x >> 3) # 0

# Binary representation of x
print(bin(x)) # 0b101

# Getting int value from binary representation
print(int('0b101', 2)) # 5