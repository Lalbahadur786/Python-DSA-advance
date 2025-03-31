"""
left = [1, 2 , 4]
right = [5, 6, 7]
task is the find max repeating number in ranges
(1, 5), (2, 6), (4, 7)
"""

def max_appear(left, right):
    """
    """
    freq = [0] * 101 # max number would be 99

    for i in range(len(left)):
        freq[left[i]] = 1
        freq[right[i]+1] = -1
    
    for j in range(1, 100):
        freq[j] =  freq[j] + freq[j-1]  #prefix sum array
    print(freq[:15])
    return freq.index(max(freq))

left = [1, 2, 4]
right = [4, 5, 7]

print(max_appear(left, right))