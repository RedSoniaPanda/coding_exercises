# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from coding_exercises.linked_list.linked_list_builder import ListNode, create_linked_list, print_linked_list


class Solution:
    def solution_to_ListNode(self, sol):
        str_sol = str(sol)
        new_array = ListNode(int(str_sol[0]))
        for n in range(1, len(str_sol)):
            new_node = ListNode(int(str_sol[n]), new_array)
            new_array = new_node
        return new_array

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        i_count = 1
        l2_num = 0
        l1_num = 0
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        while l1 is not None:
            l1_num += l1.val * i_count
            l1 = l1.next
            i_count *= 10
        i_count = 1
        while l2 is not None:
            l2_num += l2.val * i_count
            l2 = l2.next
            i_count *= 10

        return self.solution_to_ListNode(l2_num + l1_num)


def test_case_1():
    list1 = create_linked_list([])
    list2 = create_linked_list([1, 2, 3])
    sol = Solution()
    actual = sol.addTwoNumbers(list1, list2)
    assert actual.val == 1
    assert actual.next.val == 2
    assert actual.next.next.val == 3


def test_case_2():
    list1 = create_linked_list([3, 2, 4])
    list2 = create_linked_list([1, 2, 3])
    sol = Solution()
    actual = sol.addTwoNumbers(list1, list2)
    assert actual.val == 4
    assert actual.next.val == 4
    assert actual.next.next.val == 7


if __name__ == "__main__":
    test_case_1()
    test_case_2()
