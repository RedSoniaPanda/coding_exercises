from typing import List


class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def merge(self, nums1: list[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two int arrays nums1 and nums2, sorted in asc order
        # two ints m and n, that represent the # elements in num1 & num2
        # merge two arrays in asc order
        # Store in nums 1, w/length of m + n
        nums_to_keep = self.combine_nums1_nums2_m_n(m, n, nums1, nums2)
        self.create_linked_list(nums_to_keep)
        self.set_nums1_to_solution(nums1)

    def create_linked_list(self, nums):
        for num in nums:
            node = Node(num)

            if self.head is None:
                self.head = node
            elif self.tail is None:
                if self.head.val > num:
                    tmp_head = self.head
                    self.head = node
                    self.tail = tmp_head
                    self.head.next = self.tail
                    self.head.prev = self.tail
                    self.tail.prev = self.head
                    self.tail.next = self.head
                else:
                    self.tail = node
                    self.head.next = self.tail
                    self.head.prev = self.tail
                    self.tail.prev = self.head
                    self.tail.next = self.head
            else:
                tmp = self.head
                is_inserted = False
                while tmp != self.tail:
                    if tmp.val <= num <= tmp.next.val:
                        next_node = tmp.next
                        tmp.next = node
                        node.prev = tmp
                        node.next = next_node
                        next_node.prev = node
                        is_inserted = True
                        break
                    tmp = tmp.next
                if not is_inserted:
                    if self.tail.val > num >= self.tail.prev.val:
                        prev_node = self.tail.prev
                        prev_node.next = node
                        node.prev = prev_node
                        node.next = self.tail
                        self.tail.prev = node
                    elif self.tail.val <= num:
                        prev_tail = self.tail
                        self.tail = node
                        prev_tail.next = self.tail
                        self.tail.next = self.head
                        self.tail.prev = prev_tail
                    elif self.head.val > num:
                        next_head = self.head
                        self.head = node
                        self.head.prev = self.tail
                        self.head.next = next_head
                        next_head.prev = self.head

    @staticmethod
    def combine_nums1_nums2_m_n(m, n, nums1, nums2) -> List[int]:
        nums1_to_keep = nums1[:m]
        nums2_to_keep = nums2[:n]
        return nums1_to_keep + nums2_to_keep

    def set_nums1_to_solution(self, nums1):
        temp = self.head
        nums_to_keep = []
        while temp != self.tail:
            nums_to_keep.append(temp.val)
            temp = temp.next
        if self.tail is not None:
            nums_to_keep.append(self.tail.val)
        for index in range(len(nums_to_keep)):
            if index < len(nums1):
                nums1[index] = nums_to_keep[index]
            else:
                nums1.append(nums_to_keep[index])

    def print_list(self):
        print("Printing list")
        node = self.head
        while node is not self.tail:
            print(node.val)
            node = node.next
        print(self.tail.val)


def test_case_2():
    # TODO write a test case when the highest number is the first number in nums1
    nums1 = [5, 1, 3]
    nums2 = [5, 2, 6]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    sol.print_list()

    expected = [1, 2, 3, 5, 5, 6]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected

def test_case_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    Solution().merge(nums1, m, nums2, n)
    expected = [1, 2, 2, 3, 5, 6]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected


def test_case_3():
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    Solution().merge(nums1, m, nums2, n)
    expected = [1]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected


def test_case_4():
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    sol.print_list()
    expected = [1,2,3,4,5,6]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
