# WORKS!!!

from typing import List


class Solution:
    def search(self, l, r, nums) -> int:
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            if mid - 1 < 0:
                if nums[mid] < nums[r]:
                    return nums[mid]
                else:
                    return nums[r]
            if mid + 1 > len(nums) - 1:
                return nums[mid]
            if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[l] <= nums[mid]:
                # Increasing order
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        search = self.search(mid + 1, r, nums) if nums[l] <= nums[mid] else self.search(l, mid, nums)
        return search


def test_case_1():
    sol = Solution()
    actual = sol.findMin([11,12,13,14])
    assert actual == 11


def test_case_2():
    sol = Solution()
    actual = sol.findMin([4,5,6,1,2,3])
    assert actual == 1


def test_case_3():
    sol = Solution()
    actual = sol.findMin([4,5,6,7,0,1,2])
    assert actual == 0


def test_case_4():
    sol = Solution()
    actual = sol.findMin([3,4,5,1,2])
    assert actual == 1


def test_case_5():
    sol = Solution()
    actual = sol.findMin([1])
    assert actual == 1


def test_case_6():
    sol = Solution()
    actual = sol.findMin([2, 3, 4, 5, 1])
    assert actual == 1


def test_case_7():
    sol = Solution()
    actual = sol.findMin([3, 1, 2])
    assert actual == 1


def test_case_8():
    sol = Solution()
    actual = sol.findMin([9,1,2,3,4,5,6,7,8])
    assert actual == 1


def test_case_9():
    sol = Solution()
    actual = sol.findMin([266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38,39,46,49,54,65,71,74,77,79,82,83,88,92,93,94,97,104,108,114,115,117,122,123,127,128,129,134,137,141,142,144,147,150,154,160,163,166,169,172,173,177,180,183,184,188,198,203,208,210,214,218,220,223,224,233,236,241,243,253,256,257,262,263])
    assert actual == 6


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()
    test_case_9()
