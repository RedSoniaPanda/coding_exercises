from typing import List


def find_target(target: int, start: int, end: int, nums: List[int]) -> int:
    if start > end:
        # Return neg because we can't have a neg index and this will make it so I can check to not add the index to the final result
        return -1
    mid = (start + end) // 2
    if nums[mid] == target:
        return target
    elif nums[mid] < target:
        return find_target(target, mid + 1, end, nums)
    else:
        return find_target(target, start, mid - 1, nums)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        found_intersect = []

        if len(nums1) > len(nums2):
            for i in range(len(nums2)):
                if nums2[i] in found_intersect:
                    continue
                found_index = find_target(nums2[i], 0, len(nums1) - 1, nums1)
                if found_index != -1:
                    found_intersect.append(nums2[i])
        elif len(nums1) < len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in found_intersect:
                    continue
                found_index = find_target(nums1[i], 0, len(nums2) - 1, nums2)
                if found_index != -1:
                    found_intersect.append(nums1[i])
        else:
            # I need a solution when the lists are the same size
            for i in range(len(nums1)):
                if nums1[i] in found_intersect:
                    continue
                found_index = find_target(nums1[i], 0, len(nums2) - 1, nums2)
                if found_index != -1:
                    found_intersect.append(nums1[i])
        return found_intersect


def test_case_1():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersection(nums1, nums2))


def test_case_2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersection(nums1, nums2))


def test_case_3():
    nums1 = [1]
    nums2 = [1]
    print(Solution().intersection(nums1, nums2))


if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
