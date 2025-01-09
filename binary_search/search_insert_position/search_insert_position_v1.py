from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr < target:
                left += 1
            else:
                right -= 1
        # None of the below is actually needed, when the above loop ends, we're at the spot where nums[right] < target < nums[left]
        return left


        # If we hit this point it means the target's not in the list
        # I feel like the easiest way to know where to insert is through pointers?
        # Or I could use the sliding window technique but have a fixed variable window of 2
        # Case 1 - could be at the beginning
        # if target < nums[0]:
        #     return 0
        # # Case 2 is target's at the end of the list, but we can't know this w/out going through the middle
        # # Case 3 is target's somewhere in the middle
        # j = 0
        # for i in range(1, len(nums)):
        #     if nums[j] < target and nums[i] > target:
        #         return j + 1
        #     j += 1
        # if target > nums[len(nums)-1]:
        #     return len(nums)
        # return -1  # Something went horribly wrong


def test_case_1():
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    assert sol.searchInsert(nums, target) == 2


def test_case_2():
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    assert sol.searchInsert(nums, target) == 1


def test_case_3():
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    assert sol.searchInsert(nums, target) == 4


if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
