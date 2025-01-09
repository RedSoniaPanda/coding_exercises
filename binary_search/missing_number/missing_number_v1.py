# I reviewed the original problem and binary search isn't the most optimized way so this exceeds the time limit, but the solution is correct

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # Should be 0-3 ints in the list, a num will always be missing
        nums.sort()
        for i in range(n+1):
            left = 0
            right = n - 1
            is_found = False
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == i:
                    is_found = True
                    break
                if nums[mid] > i:
                    right -= 1
                else:
                    left += 1
            if not is_found:
                return i

        # Something's gone horribly wrong
        return -1


def test_case_1():
    nums = [3, 0, 1]
    sol = Solution()
    actual = sol.missingNumber(nums)
    print(actual)
    assert actual == 2


def test_case_2():
    nums = [0, 1]
    sol = Solution()
    actual = sol.missingNumber(nums)
    print(actual)
    assert actual == 2


def test_case_3():
    nums = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    actual = sol.missingNumber(nums)
    print(actual)
    assert actual == 8


if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()

