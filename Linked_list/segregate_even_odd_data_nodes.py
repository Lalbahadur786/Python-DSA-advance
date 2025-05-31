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

def segregate_even_odd_data_nodes(head):
    """
    """
    es, ee, os, oe = None, None, None, None
    curr = head

    while curr != None:
        x = curr.data

        if x % 2 == 0:
            # if this is first event elem
            if es == None:
                es = curr
                ee = es
            else:
                ee.next = curr
                ee = curr
        else:
            if os == None:
                os = curr
                oe = os
            else:
                oe.next = curr
                oe = curr
        curr = curr.next
    # check if es or os is None then
    if es == None or os == None:
        return head
    ee.next = os
    oe.next = None
    return es


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)

es = segregate_even_odd_data_nodes(head)
print_list(es)