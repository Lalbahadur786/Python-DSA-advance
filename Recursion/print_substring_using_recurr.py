# def print_subsequence(input, output):
#     """
#     """
#     # Base condition:
#     if len(input) == 0:
#         print(output)
#         return output
#     # pick second element in output
#     print_subsequence(input[1:], output+input[0])

#     # drop second element in output
#     print_subsequence(input[1:], output)

# output = ""
# input = "abcd"
# print(print_subsequence(input, output))



def print_subsequence(input, output, lst):
    """
    """
    # Base condition:
    if len(input) == 0:
        lst.append(output)
        return lst
    # pick second element in output
    print_subsequence(input[1:], output+input[0], lst)

    # drop second element in output
    print_subsequence(input[1:], output, lst)
    return lst

output = ""
input = "abcd"
lst = []
print(print_subsequence(input, output, lst))