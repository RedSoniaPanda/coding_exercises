from typing import List


class Solution:
    def search(self, l, r, target, nums2):#, results):
        while l <= r:
            mid = (l + r) // 2
            if target == nums2[mid]:
                return target
            if mid == 0:
                if mid != len(nums2) - 1 and target == nums2[mid + 1]:
                    return nums2[mid + 1]
                return -1
            elif mid == len(nums2) - 1:
                if mid != 0 and target == nums2[mid - 1]:
                    return nums2[mid - 1]
                # TODO Check
                return -1
            is_incr = nums2[mid - 1] < nums2[mid] < nums2[mid + 1]
            if is_incr and target < nums2[mid]:
                r = mid - 1
                return self.search(l, r, target, nums2)#, results)
            elif is_incr and target > nums2[mid]:
                l = mid + 1
                return self.search(l, r, target, nums2)#, results)
            else:
                result = self.search(mid + 1, r, target, nums2)#, results)
                if result != -1:
                    return result
                return self.search(l, mid - 1, target, nums2)
        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        if len(nums1) < len(nums2):
            for n in range(len(nums1)):
                l, r = 0, len(nums2) - 1
                response = self.search(l, r, nums1[n], nums2)
                if response != -1:
                    results.append(response)
        else:
            for n in range(len(nums2)):
                l, r = 0, len(nums1) - 1
                response = self.search(l, r, nums2[n], nums1)
                if response != -1 and response not in results:
                    results.append(response)
        return results


def test_case_1():
    sol = Solution()
    actual = sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])
    assert actual == [4, 9] or  [9, 4]


def test_case_2():
    sol = Solution()
    actual = sol.intersection([1,2,2,1], [2,2])
    assert actual == [2]


def test_case_3():
    sol = Solution()
    actual = sol.intersection([1,1], [2,2])
    assert actual == []


def test_case_4():
    sol = Solution()
    actual = sol.intersection([5,4,6,7,9,1], [2,2])
    assert actual == []


def test_case_5():
    sol = Solution()
    actual = sol.intersection([3,1,2], [1,3])
    assert actual == [1, 3] or [3, 1]


def test_case_6():
    sol = Solution()
    actual = sol.intersection([2, 1], [1,1])
    assert actual == [1]


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
