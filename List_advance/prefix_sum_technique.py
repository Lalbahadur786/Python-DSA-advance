"""
In this an array will be given and asked to
find getsum(0, 2) getsum(1, 4)

solution
part 1: pre- processeing
have psum array with items added from 0 till n
psum[i] = psum[i-1] + arr[i]
part 2 query the psum arr with indices
"""

arr = [2, 5, 7, 9, 9, 74, 1]
n = len(arr)
psum = [None] * n
psum[0] = arr[0]
# pre- processing the array
for i in range(1, n):
    psum[i] = psum[i-1] + arr[i]

# part 2 query the p sum

def get_sum(s, e):
    if s == 0:
        return psum[e]
    else:
        return psum[e] - psum[s-1]

print(get_sum(1, 2))