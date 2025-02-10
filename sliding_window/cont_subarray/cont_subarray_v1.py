from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        result_array = []
        result_num = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= 2:
                    result_array.append(nums[i:j+1])
                else:
                    break
            result_num += 1
        result_num += 1
        return len(result_array) + result_num


def test_case_1():
    nums = [5, 4, 2, 4]
    sol = Solution().continuousSubarrays(nums)
    print(sol)
    assert sol == 8


def test_case_2():
    nums = [1, 2, 3]
    sol = Solution().continuousSubarrays(nums)
    print(sol)
    assert sol == 6



if __name__ == "__main__":
    test_case_1()
    test_case_2()
