from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if len(seen) > k:
                seen.remove(nums[i - k])  # This is what makes it a sliding window problem
            elif nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
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
