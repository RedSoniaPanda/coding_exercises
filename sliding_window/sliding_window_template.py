def fixed_size_window(nums: list[int], k: int) -> int:
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]  # Add current element

        if i >= k - 1:  # When window reaches size k
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i - (k - 1)]  # Remove leftmost element

    return max_sum


def variable_size_window(nums, target):
    start = 0
    current_sum = 0
    min_length = float('inf')  # Initialize result with infinity

    for end in range(len(nums)):
        current_sum += nums[end]  # Expand the window by adding nums[end]

        # Shrink the window until the condition is satisfied
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)  # Update the result
            current_sum -= nums[start]  # Shrink the window
            start += 1  # Move the start pointer

    return min_length if min_length != float('inf') else 0


def two_pointer_size_window(s: str, k: int) -> int:
    char_count = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


if __name__ == "__main__":
    # Fixed size sliding window
    print("Fixed sliding window results")
    print(fixed_size_window([2, 1, 5, 1, 3, 2], 3))  # Output: 9 (5+1+3)
    print(fixed_size_window([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))  # Output: 16 (7+8+1)
    print(fixed_size_window([1, 2, 3, 4, 5], 2))  # Output: 9 (4+5)
    print(fixed_size_window([1, -1, 3, 4, -2, 2], 3))  # Output: 5 (3+4+-2)

    # Variable size sliding window
    print("Variable sliding window results")
    print(variable_size_window([2, 3, 1, 2, 4, 3], 7))  # Output: 2 ([4,3] or [3,4])
    print(variable_size_window([1, 1, 1, 1, 1, 1, 1, 1], 11))  # Output: 0 (No valid subarray)
    print(variable_size_window([1, 2, 3, 4, 5], 15))  # Output: 5 (Entire array)
    print(variable_size_window([2, 3, 1, 1, 1, 1, 2], 6))  # Output: 2 ([2,3] or [1,2])

    # two pointer
    print("two pointer sliding window results")
    print(two_pointer_size_window("eceba", 2))  # Output: 3 ("ece")
    print(two_pointer_size_window("aa", 1))  # Output: 2 ("aa")
    print(two_pointer_size_window("abcadcacacaca", 3))  # Output: 7 ("cadcaca")
    print(two_pointer_size_window("aabbcc", 2))  # Output: 4 ("aabb" or "bbcc")
