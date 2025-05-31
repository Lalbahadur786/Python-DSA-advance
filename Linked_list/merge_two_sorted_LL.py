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


def merge_two_sorted_linked_list(head1, head2):
    """
    """
    if head1 is None:
        return head2

    if head2 is None:
        return head1
    
    h, tail = None, None
    a = head1
    b = head2
    # do for first comparision only
    if a.data <= b.data:
        h = tail = a
        a = a.next
    else:
        h = tail = b
        b = b.next
    
    while a != None and b != None:
        if a.data <= b.data:
            tail.next = a
            tail = a
            a = a.next
        else:
            tail.next = b
            tail = b
            b = b.next
    
    if a.next == None:
        tail.next = b
    else:
        tail.next = a
    
    return h





# head 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(80)
head.next.next.next.next.next.next.next = Node(85)

# head2
head2 = Node(51)
head2.next = Node(52)
head2.next.next = Node(53)
head2.next.next.next = Node(64)
head2.next.next.next.next = Node(65)
head2.next.next.next.next.next = Node(66)
head2.next.next.next.next.next.next = Node(82)
head2.next.next.next.next.next.next.next = Node(84)


head = merge_two_sorted_linked_list(head, head2)
print_list(head)