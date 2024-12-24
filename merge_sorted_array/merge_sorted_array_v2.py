from typing import List


class Solution:

    def merge(self, nums1: list[int], m: int, nums2: List[int], n: int) -> None:
        nums1_to_cpy = nums1[:m]
        num1_index = 0
        num2_index = 0
        for i in range(0, m + n):
            if num2_index >= n or (
                    num1_index < m and nums1_to_cpy[num1_index] < nums2[num2_index]
            ):
                if i >= len(nums1):
                    nums1.append(nums1_to_cpy[num1_index])
                else:
                    nums1[i] = nums1_to_cpy[num1_index]
                num1_index += 1
            else:
                if i >= len(nums1):
                    nums1.append(nums2[num2_index])
                else:
                    nums1[i] = nums2[num2_index]
                num2_index += 1


def test_case_2():
    # TODO write a test case when the highest number is the first number in nums1
    # Actually, this can't be a test case, both nums 2 and 1 have to be non-decreasing and the min size for nums1 must be 6
    nums1 = [1, 3, 5, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)


    expected = [1, 2, 3, 5, 5, 6]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected

def test_case_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    Solution().merge(nums1, m, nums2, n)
    expected = [1, 2, 2, 3, 5, 6]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected


def test_case_3():
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    Solution().merge(nums1, m, nums2, n)
    expected = [1]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected


def test_case_4():
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    expected = [1,2,3,4,5,6]
    print(f"Expected {expected} Actual {nums1}")
    assert nums1 == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()