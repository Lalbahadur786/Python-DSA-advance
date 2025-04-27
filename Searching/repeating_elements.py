# This program is to find only repeating item in the arr
# elms start from 0 till  n - 2

def repeating_elem(arr):
    slow = arr[0] + 1
    fast = arr[0] + 1

    slow = arr[slow] + 1
    fast = arr[arr[fast] + 1] + 1

    # phase 1 started
    while slow != fast:
        slow = arr[slow] + 1
        fast = arr[arr[fast] + 1] + 1
    print(f"Phase 1 slow: {slow}, fast: {fast}")
    # Phase 2
    slow = arr[0] + 1
    while slow != fast:
        slow = arr[slow] + 1
        fast = arr[fast] + 1
    print(f"Phase 2 slow: {slow}, fast: {fast}")
    return slow - 1


arr = [0, 2, 1, 3, 4, 5, 6, 4]
print(repeating_elem(arr))