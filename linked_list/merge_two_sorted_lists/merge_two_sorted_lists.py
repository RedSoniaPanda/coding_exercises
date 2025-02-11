from typing import Optional, List
from linked_list.linked_list_builder import ListNode, create_linked_list, print_linked_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            new_array = ListNode(list1.val)
            list1 = list1.next
        else:
            new_array = ListNode(list2.val)
            list2 = list2.next
        new_array_node = new_array
        while list1 is not None or list2 is not None:
            if list1 is None:
                # Add remaining list2 items
                new_node = ListNode(list2.val, None)
                new_array_node.next = new_node
                new_array_node = new_array_node.next
                list2 = list2.next
            elif list2 is None:
                # Add remaining list2 items
                new_node = ListNode(list1.val, None)
                new_array_node.next = new_node
                new_array_node = new_array_node.next
                list1 = list1.next
            elif list1.val < list2.val:
                new_node = ListNode(list1.val, None)
                new_array_node.next = new_node
                new_array_node = new_array_node.next
                list1 = list1.next
            elif list1.val > list2.val:
                new_node = ListNode(list2.val, None)
                new_array_node.next = new_node
                new_array_node = new_array_node.next
                list2 = list2.next
            elif list1.val == list2.val:
                new_node = ListNode(list1.val, None)
                new_array_node.next = new_node
                new_array_node = new_array_node.next
                list1 = list1.next

                new_node = ListNode(list2.val, None)
                new_array_node.next = new_node
                new_array_node = new_array_node.next
                list2 = list2.next
        return new_array


def test_case_1():
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    sol = Solution()
    actual = sol.mergeTwoLists(list1, list2)
    assert actual == None


def test_case_2():
    list1 = create_linked_list([1, 1])
    list2 = create_linked_list([])
    sol = Solution()
    actual = sol.mergeTwoLists(list1, list2)
    print_linked_list(actual)
    assert actual.val == 1 and actual.next.val == 1


def test_case_3():
    list1 = create_linked_list([2, 3])
    list2 = create_linked_list([1])
    sol = Solution()
    actual = sol.mergeTwoLists(list1, list2)
    print_linked_list(actual)


def test_case_4():
    list1 = create_linked_list([1])
    list2 = create_linked_list([2, 3])
    sol = Solution()
    actual = sol.mergeTwoLists(list1, list2)
    print_linked_list(actual)


def test_case_5():
    list1 = create_linked_list([40, 41, 42, 43])
    list2 = create_linked_list([2, 3])
    sol = Solution()
    actual = sol.mergeTwoLists(list1, list2)
    print_linked_list(actual)



if __name__ == "__main__":
    # Example usage:
    # values = [1, 2, 3, 4, 5]
    # linked_list_head = create_linked_list(values)
    #
    # Print the linked list
    # print_linked_list(linked_list_head)

    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
