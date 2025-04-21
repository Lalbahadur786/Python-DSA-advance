"Given the total number of persons N and a number k which indicates that k-1 persons are skipped and the kth person is killed in a circle. The task is to choose the person in the initial circle that survives."

def jos(n, k):
    # Base case: If there is only one person left, they are the survivor (position 0)
    if n == 1:
        return 0
    else:
        # Recursive case: Find the position of the survivor in the smaller circle
        # and adjust the position according to the current circle size
        return (jos(n-1, k)+k) % n

# Call the josephus function with 5 people and every 2nd person is eliminated
print(jos(5, 2))

def jos_begin_with_one(n, k):
    return jos(n, k) + 1

print(jos_begin_with_one(5, 2))