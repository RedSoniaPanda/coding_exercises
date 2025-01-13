# https://leetcode.com/problems/find-peak-element/editorial/
from typing import List


class Solution:
    def search(self, nums, left, right):
        if left == right:
            return left
        mid = (right + left) // 2
        if nums[mid] < nums[mid + 1]:
            # mid is not greater than the left neighbor
            return self.search(nums, left, mid)
        return self.search(nums, mid + 1, right)

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        found_element = self.search(nums, left, right)
        return found_element


def test_case_1():
    nums = [1,2,3,1]
    sol = Solution()
    assert sol.findPeakElement(nums) == 2


def test_case_2():
    nums = [1,2,1,3,5,6,4]
    sol = Solution()
    peak_elem = sol.findPeakElement(nums)
    assert peak_elem == 5 or peak_elem == 2


if __name__ == "__main__":
    # test_case_1()
    test_case_2()
