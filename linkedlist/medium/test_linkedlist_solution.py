import pytest
from linkedlist.medium.solution import *

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_addTwoNumbers() :
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    result = addTwoNumbers(l1, l2)

    output = linked_list_to_list(result)

    assert output == [7, 0, 8]

    
