"""
count the number of set bits in binary representation of a number
"""

# Naive approach O(number of bits)
def naive_soln_count_set_bits(n):
    """
    n = 5
         101
         001
         001 then increase counter by 1
    """
    count = 0
    while n:
        if n & 1:   # n % 2 does the same work
            count += 1
        n = n // 2
    return count

# better solution 0(number of set bits)
def brian_kernigams_algo_to_count_set_bits(n):
    """
    n = 32
           32 = 100000
        and with n-1 i.e. 31
           32 = 100000
        &  31 = 011111
              = 000000  only one iteration rquired
    """
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res

# more efficient solution O(1)
def lookup_table_soln_for_count_set_bits(n):
    # Preassumption number wont be longer than 32 bits
    tbl = [0] * 256 # Creating lookup table for first 8 bit

    # Fill the lookup table
    for i in range(256):
        tbl[i] = (i & 1) + tbl[i // 2]

    # Count bits
    # oxff = 11111111 8bits with all set
    # This is right shifting 8 bits at time till 32 bit
    # if it is 64 bit then shift again in chunks of 8 till 64 bits
    return (tbl[n & 0xff] + tbl[(n >> 8) & 0xff] + tbl[(n >> 16) & 0xff] + tbl[(n >> 24) & 0xff])



if __name__ == "__main__":
    n = 15
    # print(naive_soln_count_set_bits(n))
    # print(brian_kernigams_algo_to_count_set_bits(n))
    print(lookup_table_soln_for_count_set_bits(n))
        