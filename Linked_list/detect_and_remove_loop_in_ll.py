class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    print()


def loop_detect_and_removal(head):
    """
    """
    slow = head
    fast = head
    
    # Fisrt detect the loop
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    if slow != fast:
        # No loop
        return
    
    # loop removal
    slow = head
    while slow.next != fast.next :
        slow = slow.next
        fast = fast.next   # increment by one not 2
    fast.next = None  # Removing the loop





head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next.next = head.next.next.next # Creating cycle

loop_detect_and_removal(head)

print_list(head)