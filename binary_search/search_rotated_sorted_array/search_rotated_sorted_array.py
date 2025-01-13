from typing import List


class Solution:
    def find_min_point(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def search(self, nums: List[int], target: int) -> int:
        # Case 1 - the pivot point is the beginning of the array if the array starts with 0
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        min_index = self.find_min_point(nums)

        # TODO experiment with finding the max index
        left = min_index
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left += 1
            else:
                right -= 1


def test_case_1_5():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 6
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == 4


def test_case_1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == 4


def test_case_2():
    nums = [4,5,6,7,0,1,2]
    target = 3
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == -1


def test_case_3():
    nums = [1]
    target = 0
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == -1


def test_case_4():
    nums = [1, 3]
    target = 1
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == 0


def test_case_5():
    nums = [1, 3]
    target = 0
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == -1


def test_case_6():
    nums = [1, 3, 5]
    target = 1
    sol = Solution()
    actual = sol.search(nums, target)
    assert actual == 0


if __name__ == "__main__":
    test_case_1_5()
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    # test_case_5()
    # test_case_6()
