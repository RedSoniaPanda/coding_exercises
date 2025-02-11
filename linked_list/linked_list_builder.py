from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: List[int]):
    """Creates a linked list from a list of integers and returns the head node."""
    if not values:
        return None  # Return None if the list is empty

    head = ListNode(values[0])  # Create the head node
    current = head

    for val in values[1:]:
        current.next = ListNode(val)  # Create and link the new node
        current = current.next  # Move to the next node

    return head  # Return the head of the linked list


def print_linked_list(head):
    # Function to print the linked list for verification
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()
