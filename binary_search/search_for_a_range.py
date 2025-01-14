from typing import List


class Solution:
    def search(self, nums, target, is_first):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if is_first:
                    if mid == 0 or nums[mid - 1] < target:
                        return mid
                    right = mid - 1  # Search right
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid
                    left = mid + 1  # Search left
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        # if nums[mid] == target and nums[mid - 1] == target:
        # search for lower bound in left half
        # if nums[mid] == target and nums[mid+1] >< target:
        # search for upper bound in right half
        lower_bound = self.search(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.search(nums, target, False)

        return [lower_bound, upper_bound]


def test_case_1():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


def test_case_2():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    expected = [-1, -1]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


def test_case_3():
    nums = []
    target = 0
    expected = [-1, -1]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


def test_case_4():
    nums = [5, 7, 7, 8, 8, 10]
    target = 5
    expected = [0, 0]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


def test_case_5():
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    expected = [5, 5]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


def test_case_6():
    nums = [1]
    target = 1
    expected = [0, 0]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


def test_case_7():
    nums = [1, 1, 2]
    target = 1
    expected = [0, 1]
    sol = Solution()
    actual = sol.searchRange(nums, target)
    assert actual == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
