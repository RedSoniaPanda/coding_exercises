# This solution works, but exceeds the time limit.

from typing import List


class Solution:
    def __init__(self):
        self.all_sums = []

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        window_size = 1
        start = 0
        end = window_size
        mod = 10**9 + 7

        while window_size <= n:
            window_sum = 0

            for i in range(start, end):
                window_sum += nums[i]
            self.all_sums.append(window_sum)
            if end != n:
                start += 1
                end += 1
            else:
                window_size += 1
                start = 0
                end = window_size

        self.all_sums.sort()
        return sum(self.all_sums[left-1:right]) % mod


def get_final_sum(left, n, nums, right):
    sol = Solution()
    final_sum = sol.rangeSum(nums, n, left, right)
    print(sol.all_sums)
    print(final_sum)
    return final_sum


def test_case_1():
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5
    final_sum = get_final_sum(left, n, nums, right)
    assert final_sum == 13


def test_case_2():
    nums = [1, 2, 3, 4]
    n = 4
    left = 3
    right = 4
    final_sum = get_final_sum(left, n, nums, right)
    assert final_sum == 6


def test_case_3():
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 10
    final_sum = get_final_sum(left, n, nums, right)
    assert final_sum == 50


if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
