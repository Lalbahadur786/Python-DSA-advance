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

def reverse_by_k_itr(head, k):
    """
    """
    curr = head
    prev_first = None
    first_pass = True
    while curr != None:
        first, prev = curr , None
        count = 0
        while curr != None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        if first_pass:
            head = prev
            first_pass = False
        else:
            prev_first.next = prev
        prev_first = first
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)

head = reverse_by_k_itr(head, 3)
print_list(head)