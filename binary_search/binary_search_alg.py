from typing import List


def binary_search_v1(nums: List[int], target: int):
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


def binary_search_v2(nums: List[int], target: int):
    # The beginning is the same, if the list can be empty, ret -1
    if len(nums) == 0:
        return -1

    # The left and right are the same starting point as well
    left, right = 0, len(nums) - 1
    # Search space is always 3 in size at each step
    # Loop ends when there are 2 elements left, which is why post-processing is done on the last two values
    # Termination: left + 1 == right
    while left + 1 < right:
        # loop is the same
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Searching left
            left = mid  # Set both to the mid-point
        else:
            # Searching right
            right = mid  # Set both to the mid-point

    # Things really differ here, we post-process the data for the right answer
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1


def main():
    test_case_1()
    test_case_2()


# TODO Find a better test case for binary_v2
def test_case_2():
    nums = [-1,0,3,5,9,12]
    target = 9
    found = binary_search_v1(nums, target)
    assert found == 4
    found = binary_search_v1(nums, target)
    assert found == 4


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    found = binary_search_v1(nums, 2)
    assert found == -1


if __name__ == '__main__':
    main()
