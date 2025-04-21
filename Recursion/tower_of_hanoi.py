# def toh(n, A, B, C):
#     if n == 1:
#         print(f"Move from {A} to {C}")
#     else:
#         toh(n-1, A, C, B)
#         print(f"Move from {A} to {C}")
#         toh(n-1, B, A, C)


# print(toh(3, 'A', 'B', 'C'))


def toh(n, A, B, C):
    if n == 1:
        print(f"Move from {A} to {C}")
        return 1
    else:
        moves = 0
        moves +=  toh(n-1, A, C, B)
        moves += 1
        print(f"Move from {A} to {C}")
        moves += toh(n-1, B, A, C)
    return moves


print(toh(1, 'A', 'B', 'C'))