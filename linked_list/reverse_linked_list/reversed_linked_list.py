# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from coding_exercises.linked_list.linked_list_builder import ListNode, create_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_array = ListNode(head.val, None)
        curr = head.next
        while curr is not None:
            new_node = ListNode(curr.val, new_array)
            new_array = new_node
            curr = curr.next
        return new_array


def test_case_1():
    list1 = create_linked_list([40, 41, 42, 43])
    sol = Solution()
    actual = sol.reverseList(list1)
    print_linked_list(actual)


if __name__ == "__main__":
    test_case_1()
