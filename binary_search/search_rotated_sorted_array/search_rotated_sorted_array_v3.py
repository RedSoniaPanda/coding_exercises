from typing import List


class Solution:
    def find_inflection(self, nums, left, right):
        # if left == right:
        #     return left, right
        # mid = left + (right - left) // 2
        # # I don't know if I'll actually need the two below lines
        # if nums[mid - 1] > nums[mid] < nums[mid + 1]:
        #     return mid, right
        # if nums[mid + 1] > nums[mid]:
        #     # go right by reducing left search space
        #     return self.find_inflection(nums, left, mid + 1)
        # return self.find_inflection(nums, mid, right)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return left, right

    def binary_search(self, left, right, nums, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # First I need to find the inflection point, otherwise we won't know when to go left or right
        # Once the inflection point is found, then we can determine whether to go right or left
        # Inflection point will have integers higher than it on both sides
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        if nums[0] > nums[-1]:
            left, right = self.find_inflection(nums, 0, len(nums) - 1)
        else:
            left = 0

        if (answer := self.binary_search(0, left - 1, nums, target)) != -1:
            return answer
        return self.binary_search(left, len(nums) - 1, nums, target)


def test_case_1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    expected = 4
    run_test_case(nums, target, expected)


def test_case_2():
    nums = [1]
    target = 0
    expected = -1
    run_test_case(nums, target, expected)


def test_case_3():
    nums = [4,5,6,7,0,1,2]
    target = 7
    expected = 3
    run_test_case(nums, target, expected)


def test_case_4():
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    target = 7
    expected = 7
    run_test_case(nums, target, expected)


def test_case_5():
    nums = [3, 1]
    target = 0
    expected = -1
    run_test_case(nums, target, expected)


def test_case_6():
    nums = [3, 1]
    target = 1
    expected = 1
    run_test_case(nums, target, expected)


def test_case_7():
    nums = [3, 1]
    target = 3
    expected = 0
    run_test_case(nums, target, expected)


def run_test_case(nums, target, expected):
    sol = Solution()
    actual = sol.search(nums, target)
    print(actual)
    assert expected == actual


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
