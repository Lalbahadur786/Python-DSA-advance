def check_kth_bit_set_or_not_using_left_shift_operator(n, k):
    return (n & (1 << (k - 1))) != 0

def check_kth_bit_set_or_not_using_right_shift_operator(n, k):
    return ((n >> (k - 1)) & 1) != 0


if __name__ == "__main__":
    n = 10
    k = 3
    print(check_kth_bit_set_or_not_using_left_shift_operator(n, k))
    print(check_kth_bit_set_or_not_using_right_shift_operator(n, k))