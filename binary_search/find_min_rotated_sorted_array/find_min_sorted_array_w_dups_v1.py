from typing import List


class Solution:
    def search(self, l, r, nums) -> int:
        while l <= r:
            # Quick returns
            if nums[l] < nums[r]:  # 1
                return nums[l]
            mid = (l + r) // 2
            if mid - 1 < 0:  # 2
                if nums[mid] < nums[r]:
                    return nums[mid]
                else:
                    return nums[r]
            if mid + 1 > len(nums) - 1:  # 3
                return nums[mid]

            # Search condition
            if nums[mid - 1] > nums[mid] <= nums[mid + 1]:  # 4
                return nums[mid]

            # Reduce search space for left or right side
            if nums[l] < nums[mid] and nums[r] < nums[mid]:  # 5
                l = mid
            elif nums[l] == nums[mid]: #  and nums[mid] > nums[r]:  # 6
                l = mid + 1
            # elif nums[l] == nums[mid] and nums[mid] < nums[r]:  # 6
            #     l = mid + 1
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
        search = -1
        if nums[l] < nums[mid]:
            search = self.search(mid + 1, r, nums)
        elif nums[l] != nums[mid] and (nums[l] > nums[mid] < nums[r]):
            search = self.search(l, mid, nums)
        elif nums[l] != nums[mid] and (nums[l] > nums[mid] > nums[r]):
            search = self.search(mid, r, nums)
        else:
            search_l = self.search(l, mid, nums)
            search_r = self.search(mid + 1, r, nums)
            if (search_l != -1 and search_l < search_r) or search_r == -1:
                search = search_l
            else:
                search = search_r
        return search


def test_case_8():
    sol = Solution()
    actual = sol.findMin([3,3,3,3,3,3,3,3,1,3])
    assert actual == 1


def test_case_9():
    sol = Solution()
    actual = sol.findMin([2,2,0,1,2])
    assert actual == 0


def test_case_10():
    sol = Solution()
    actual = sol.findMin([2,2,2,0,1])
    assert actual == 0


def test_case_11():
    sol = Solution()
    actual = sol.findMin([10,1,10,10,10])
    assert actual == 1


if __name__ == "__main__":
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    # test_case_5()
    # test_case_6()
    # test_case_7()
    test_case_8()
    test_case_9()
    test_case_10()
    test_case_11()
