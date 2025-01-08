from typing import List


"""Given an array of integers of size ‘n’,
calculate the maximum sum of ‘k’ consecutive elements in the array."""



class Solution:
    def max(self, arr: List[int], n: int, k:int) -> int:
        max_num = min(arr)

        for i in range(n - k + 1):
            current_sum = 0
            for j in range(k):
                current_sum += arr[i + j]
            max_num = max(current_sum, max_num)

        return max_num


def test_case_1():
    nums = [1, 4, 2, 10, 2,
            3, 1, 0, 20]
    n = len(nums)
    k = 4
    assert Solution().max(nums, n, k) == 24


if __name__ == '__main__':
    test_case_1()
