from typing import List


class Solution:
    def count_and_sum(self, nums, n, target):
        count = 0
        current_sum = 0
        total_sum = 0
        window_sum = 0
        i = 0
        for j in range(n):
            current_sum += nums[j]
            window_sum += nums[j] * (j - i + 1)
            while current_sum > target:
                window_sum -= current_sum
                current_sum -= nums[i]
                i += 1
            count += j - i + 1
            total_sum += window_sum
        return count, total_sum

    def sum_of_first_k(self, nums, n, k):
        start = min(nums)
        end = max(nums)

        while start <= end:
            mid = start + (end - start) // 2
            if self.count_and_sum(nums, n, mid)[0] >= k:
                end = mid - 1
            else:
                start = mid + 1
        count, total_sum = self.count_and_sum(nums, n, start)
        # There can be more sub-arrays with the same sum of left.
        return total_sum - start * (count - k)

    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7  # This is given in the problem description! Just code it first and get it out of the way

        result = (
            self.sum_of_first_k(nums, n, right) - self.sum_of_first_k(nums, n, left - 1)
        ) % mod
        # Ensure non-negative result - how?
        return (result + mod) % mod


def test_case_1():
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5
    assert Solution().rangeSum(nums, n, left, right) == 13


if __name__ == '__main__':
    test_case_1()
