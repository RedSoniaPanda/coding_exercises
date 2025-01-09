from typing import List


def binary_search(nums: List[int], target: int):
    # Set the left and right boundaries
    left = 0
    right = len(nums) - 1

    # Under this condition
    while left <= right:
        # Get the middle index and the middle value.
        mid = (left + right) // 2

        # Case 1, return the middle index.
        if nums[mid] == target:
            return mid
        # Case 2, discard the smaller half.
        elif nums[mid] < target:
            left = mid + 1
            # Case 3, discard the larger half.
        else:
            right = mid - 1

    # If we finish the search without finding target, return -1.
    return -1


def main():
    # test_case_1()
    test_case_2()


def test_case_2():
    nums = [-1,0,3,5,9,12]
    target = 9
    mid = len(nums) // 2
    found = binary_search(nums, target)
    assert found == 4


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    mid = len(nums) // 2
    found = binary_search(nums, 2)
    assert found == -1


if __name__ == '__main__':
    main()
