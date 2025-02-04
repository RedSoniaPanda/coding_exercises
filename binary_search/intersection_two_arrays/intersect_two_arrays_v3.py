from typing import List


class Solution:
    def search(self, target, nums, l, r, result):
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return target
        if mid == 0:
            if nums[mid + 1] == target:
                return target
            return -1
        if mid == len(nums) - 1:
            if nums[mid - 1] == target:
                return target
            return -1
        # if nums[mid - 1] > nums[mid] < nums[mid + 1]:
        result = self.search(target, nums, l, mid - 1, result)
        if result == -1:
            result = self.search(target, nums, mid + 1, r, result)
        # incr_array = nums[mid - 1] < nums[mid] < nums[mid + 1]
        # if incr_array and target < nums[mid]:  # increasing array
        #     result = self.search(target, nums, l, mid - 1, result)
        #
        # if incr_array and target > nums[mid]:  # increasing array
        #     result = self.search(target, nums, mid + 1, r, result)
        return result

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) == 0 or len(nums2) == 0:
            # No intersection point
            return result
        l = 0
        if len(nums1) < len(nums2):
            r = len(nums2) - 1
            for i in range(len(nums1)):
                result_num = -1
                tmp_result = self.search(nums1[i], nums2, l, r, result_num)
                if tmp_result != -1 and tmp_result not in result:
                    result.append(tmp_result)
        else: # len(nums1) >= len(nums2):
            r = len(nums1) - 1
            for i in range(len(nums2)):
                result_num = -1
                tmp_result = self.search(nums2[i], nums1, l, r, result_num)
                if tmp_result != -1 and tmp_result not in result:
                    result.append(tmp_result)
        return result


def test_case_1():
    sol = Solution()
    actual = sol.intersection([6, 1], [3, 1, 2])
    print(f"actual {actual}")
    assert actual == [1]


def test_case_2():
    sol = Solution()
    actual = sol.intersection([3, 1, 2], [6, 1])
    print(f"actual {actual}")
    assert actual == [1]


def test_case_3():
    sol = Solution()
    nums1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
    nums2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]
    actual = sol.intersection(nums1, nums2)
    print(f"actual {actual}")
    assert actual == [61,45,85,89,5,77,92,38,7,34,44,57,4,6,88,0,79]


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
