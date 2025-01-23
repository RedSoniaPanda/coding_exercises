# [Problem Link](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1033/)

# Problem Constraints

 - n == nums.length
 - 1 <= n <= 5000
 - -5000 <= nums[i] <= 5000
 - All the integers of nums are unique.
 - nums is sorted and rotated between 1 and n times.
 - Array is increasing order
 - Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
 - must write an algorithm that runs in O(log n) time
 - there would be a point in the array where there is a small deflection from the increasing sequence
 - All the elements to the left of inflection point > first element of the array. 
 - All the elements to the right of inflection point < first element of the array.

# Intuition

 - The starting point of where to search could be at the beg, middle, or end of the list
 - All elem to the right of the inflection point < first elem in array
 - The mid point is also the minimum number in an increasing array
 - if nums[0] < nums[-1] : return nums[0] Just return this if this is True
 - If len(nums) == 1: return nums[0]
 - How to know? Need to find the min point
   - ONLY search right if l > r, otherwise, search left

# [Second Problem Link](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/)

# Problem Constraints

 - There can be duplicate entries
 - the array is still in ascending order
 - n == nums.length
 - 1 <= n <= 5000
 - -5000 <= nums[i] <= 5000
 - nums is sorted and rotated between 1 and n times.

# Intuition
 - The left and right search condition from before applies, but there should be an additional check
 - if nums[mid - 1] > nums[mid] <= nums[mid + 1] - Changes w/less than or equal on the right
 - if nums[l] == nums[r] and nums[l] > nums[mid]: r = m - 1
 - if nums[l] == nums[r] and nums[l] < nums[mid]: l = m + 1
 - if nums[l] <= nums[mid]: l = mid + 1  # OG
 - else: r = mid - 1