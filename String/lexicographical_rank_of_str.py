
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

def find_smaller_in_right(st, low, high):
    countRight = 0
    i = low + 1
    while i <= high:
        if st[i] < st[low]:
            countRight += 1
        i += 1
    return countRight

def lexicographical_rank(st):
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0
    while i < ln:
        mul = mul // (ln - i)

        # count num of chars smaller
        # than str[i] from str[i+1] to str[len-1]
        count_right = find_smaller_in_right(st, i, ln-1)

        rank = rank + count_right * mul
        i += 1
    return rank

st = "string"
print (lexicographical_rank(st))