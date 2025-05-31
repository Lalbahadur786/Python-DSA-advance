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


def pairwise_swap(head):
    """
    """
    if head == None or head.next == None:
        return head
    
    curr = head.next.next
    prev = head
    head = head.next
    head.next = prev

    while curr != None and curr.next != None:
        prev.next = curr.next
        prev = curr
        next = curr.next.next
        curr.next.next = curr
        curr = next
    prev.next = curr
    return head



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)

head = pairwise_swap(head)

print_list(head)