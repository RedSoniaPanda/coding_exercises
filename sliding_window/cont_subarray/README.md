# [Problem Link](https://leetcode.com/problems/continuous-subarrays/)

# Constraints
 - 1 <= nums.length <= 105
 - 1 <= nums[i] <= 109
 - for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2
 - Return the total number of continuous subarrays.
 - A subarray is a contiguous non-empty sequence of elements within an array

# Intuition
 - If the list is size 1, return 1
 - n = len(nums)
 - First: sum the length of the array, because each item in the array is a subarray on it's own
    - Ex: [5, 4, 2, 4] subarray 1 is [5], [4], [3], [2], [1]
 - Second: the window size is variable, it should increase each loop for i in range(n - 1): window_size = i; 
   - Window size can't be larger than the array result_arr
   - loop inside starts at i + 1 for j in range(i + 1, n): result_array.append(nums[i:j] if abs(nums[i] - nums[j]) <= 2 else break) 
   - result += 1 each iteration
   - result += len(result_arr)
   - result_array = []
 - 
