"""
Mathod 1 using hashing or set
By pushinh head1 into set and traverse 2 LL
and check if present or not
O(n+m) O(m)

method 2 using d distance
make sure head1 is always greater
"""
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

def find_inersection_point(d, head1, head2):
    """
    """
    curr1 = head1
    curr2 = head2

    # move curr1 by d nodes

    for  i in range(d):
        if curr1 == None:
            return -1
        curr1 = curr1.next

    #  now move curr1 and curr2 by 1

    while curr1 != None and curr2 != None:
        if curr1 == curr2:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next


#head2
head2 = Node(10)
head2.next = Node(20)
head2.next.next = Node(30)

# head1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(50)
head2.next.next.next = head.next.next.next  # intersecting point
head.next.next.next.next = Node(60)
head.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(7)

c1 = 0
c2 = 0
# count nodes in head1
curr = head
while curr != None:
    c1 += 1
    curr = curr.next

# count nodes in head2
curr = head2
while curr != None:
    c2 += 1
    curr = curr.next

d = abs(c1-c2)

print(find_inersection_point(d, head, head2))