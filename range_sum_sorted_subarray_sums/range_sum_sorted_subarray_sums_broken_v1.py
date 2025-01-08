from typing import List


class Solution:
    def __init__(self):
        self.running_sum = 0
        self.sums = []
        self.index_added = []

    def rec_sum(self, start, end, size, nums):
        if start == size:
            self.running_sum += nums[start]
            self.sums.append(self.running_sum)
            if start != 0 and end == size:
                self.running_sum = 0
                return self.rec_sum(0, end-1, size, nums)
            return self.sums
        self.running_sum += nums[start]
        if start not in self.index_added:
            self.index_added.append(start)
            self.sums.append(nums[start])


        return self.rec_sum(start+1, end, size, nums)

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        all_sums = self.rec_sum(0, n - 1, n - 1, nums)
        # all_sums.extend(nums[left:right])
        all_sums.sort()
        print(all_sums)
        return sum(all_sums[left-1:right])


def test_case_1():
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5
    assert Solution().rangeSum(nums, n, left, right) == 13


if __name__ == '__main__':
    test_case_1()
