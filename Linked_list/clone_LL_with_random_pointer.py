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


def clone_ll_with_random_using_hashing(head):
    """
    """
    # random links avoided
    curr = head
    d = {None: None}

    # create dict of nodes
    while curr != None:
        d[curr] = Node(curr.data)
        curr = curr.next
    
    # connect the  linkes
    curr = head
    while curr != None:
        d[curr].next = curr.next
        # d[curr].random = curr.random
        curr = curr.next
    return d[head]


def clone_ll_with_random_efficient(head):
    """
    """
    # random links avoided
    curr = head
    #clone the node and place in between
    while curr != None:
        next = curr.next
        curr.next = Node(curr.data)
        curr.next.next = next
        curr = next
    
    # step 2 handle random links
    """
    use when we have random links
    curr = head
    while curr != None:
        curr.next.random = curr.random.next
        curr = curr.next.next
    """

    h2 = head.next
    clone = h2
    curr = head
    while curr != None:
        curr.next = curr.next.next
        clone.next = None if clone.next == None else clone.next.next
        clone = clone.next
        curr = curr.next
    return h2


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)


# cl_head = clone_ll_with_random_using_hashing(head)

cl_head = clone_ll_with_random_efficient(head)

print_list(cl_head)