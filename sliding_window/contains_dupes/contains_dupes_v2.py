from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = set()

        for i in range(len(nums)):
            if nums[i] in result:
                return True
            result.add(nums[i])
            if len(result) > k:
                result.remove(nums[i - k])
        return False


def test_case_1():
    sol = Solution()
    assert False == sol.containsNearbyDuplicate([1,2,3,1,2,3], 2)


def test_case_2():
    sol = Solution()
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3)


if __name__ == "__main__":
    test_case_1()
    test_case_2()
