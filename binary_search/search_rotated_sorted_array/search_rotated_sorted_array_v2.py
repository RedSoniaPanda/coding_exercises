from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[left]:
            return nums[left]
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


def test_case_1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    actual = sol.findMin(nums)
    assert actual == 0


def test_case_3():
    nums = [1]
    sol = Solution()
    actual = sol.findMin(nums)
    assert actual == 1


def test_case_4():
    nums = [3,4,5,1,2]
    sol = Solution()
    actual = sol.findMin(nums)
    assert actual == 1


def test_case_5():
    nums = [2,3,4,5,1]
    sol = Solution()
    actual = sol.findMin(nums)
    assert actual == 1


def test_case_6():
    nums = [1, 3, 5]
    sol = Solution()
    actual = sol.findMin(nums)
    assert actual == 1


def test_case_7():
    nums = [11,13,15,17]
    sol = Solution()
    actual = sol.findMin(nums)
    assert actual == 11



if __name__ == "__main__":
    # test_case_1()
    # test_case_3()
    test_case_4()
    test_case_5()
    # test_case_6()
    test_case_7()
