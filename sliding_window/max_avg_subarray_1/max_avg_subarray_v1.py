from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_sum = sum(nums[:k])
        n = len(nums)

        max_avg = running_sum / k
        for i in range(1, n):
            if i + (k - 1) > n - 1:
                break
            running_sum = running_sum - nums[i - 1] + nums[i + (k - 1)]
            max_avg = max(max_avg, running_sum / k)

        return max_avg


def test_case_1():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    actual = Solution().findMaxAverage(nums, k)
    print(actual)
    assert actual == 12.75000


if __name__ == "__main__":
    test_case_1()
