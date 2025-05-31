class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop_floyds_algo(head):
    """
    """
    slow = head
    fast = head

    while fast and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False




head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)
# head.next.next.next.next.next.next.next.next = head # Creating cycle

print(detect_loop_floyds_algo(head))