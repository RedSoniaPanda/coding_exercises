from typing import List


"""
These 3 templates differ by their:

    - left, mid, right index assignments
    - loop or recursive termination condition
    - necessity of post-processing

Other Facts
-----------

Runtime: O(log n) - logarithmic time
Space: O(1) -- Constant Space
Search space reduces in half
In other use cases the left/right may increase or decrease by 1 instead of using the mid point
"""


def binary_search_v1(nums: List[int], target: int):
    """
    Most basic form
    Search condition can be determined w/out comparing to neighbors or use elements around it
    No post-processing required, at each step, check to see if the element is found, if you reach the end the element isn't found
    """
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
    """
    Advanced implementation of binary search
    Search condition needs to access element's right neighbor
    Use right neighbor to determine if conditions is met, then decide to go left/right
    Guarantees search space is 2 in size at each step
    Post processing required. Loop ends when there's one element left, and we need to check the remaining element meets the condition
    """
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


def binary_search_v3(nums: List[int], target: int):
    """
    Alternative way to implement binary search
    Search condition needs to access left and right neighbors
    Use element's neighbors to determine if the condition is met and decide whether to go left/right
    Guaranteed search space of 3 at each step
    Post-processing required - Loop/recursion ends when 2 elements are left. Assess remaining elements meet condition
    """
    # Potential pre-processing in each binary search
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    # Post process the results to see if left or right
    # left + 1 == right
    # 2 candidates will remain
    if nums[left] == target: return left
    if nums[left + 1] == target: return left + 1
    # OR
    if nums[right] == target: return left + 1


def binary_v1_tests():
    test_case_1()
    test_case_2()


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    found = binary_search_v1(nums, 2)
    assert found == -1


def test_case_2():
    nums = [-1,0,3,5,9,12]
    target = 9
    found = binary_search_v1(nums, target)
    assert found == 4
    found = binary_search_v1(nums, target)
    assert found == 4


# TODO Find a better test case for binary_v2
def main():
    binary_v1_tests()


if __name__ == '__main__':
    main()
