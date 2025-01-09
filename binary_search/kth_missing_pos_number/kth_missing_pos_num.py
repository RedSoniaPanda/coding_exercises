from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Take the index and start with 0 and it can go up to 1000 ** here's where I want to see if I can optimize?
        # Check if it's missing in the array
        # if it's in the array, then don't check if we've reached k elements
        # if it's not in the array, then add it to the missing_nums and check
        # if we've reached k elements in the missing_nums, if yes, return the last num


        # We can compare a full array of ints against the arr by looking at the element of arr
        # by substracting the element of the full array from arr
        # If the num of pos ints that are missing before arr[pivot] is less than k then search on right side of the array
        # Otherwise search left
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2  # This is the element of the full array
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k


def test_case_1():
    arr = [2, 3, 4, 7, 11]
    k = 5
    sol = Solution()
    actual = sol.findKthPositive(arr, k)
    print(actual)
    assert actual == 9


if __name__ == "__main__":
    test_case_1()
