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

def reversed_ll(head):
    """
    """
    prev = None

    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def is_palindrome_linked_list(head):
    """
    """
    if head == None:
        return head
    
    slow, fast = head, head
    
    # determine mid of the linked list
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    # Now slow is at mid point
    # reverse LL from slow.next
    rev_ll = reversed_ll(slow.next)

    curr = head
    while rev_ll != None:
        if rev_ll.data != curr.data:
            return False
        rev_ll = rev_ll.next
        curr = curr.next
    return True
   






head = Node('M')
head.next = Node('A')
head.next.next = Node('D')
head.next.next.next = Node('A')
head.next.next.next.next = Node('M')

print(is_palindrome_linked_list(head))