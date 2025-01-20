from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left = 0
        right = n
        while left < right:
            mid = left + right // 2
            if mid != n and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if mid != n and nums[mid + 1] > nums[mid]:
                left += 1
            else:
                right -= 1
        return n


def test_case_1():
    nums = [1,2,3,1]
    expected = 2
    actual = Solution().findPeakElement(nums)
    assert actual == expected


def test_case_2():
    # No peak
    nums = [1,2,3]
    expected = 2
    actual = Solution().findPeakElement(nums)
    assert actual == expected


def test_case_3():
    # Multiple peaks, chose one
    nums = [1,2,1,3,5,6,4]
    expected = 5 or 0
    actual = Solution().findPeakElement(nums)
    assert actual == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
