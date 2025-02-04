[Problem Link](https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/)

# Problem Constraints

 - 1 <= nums1.length, nums2.length <= 1000
 - 0 <= nums1[i], nums2[i] <= 1000

# Intuition

 - If len(nums2) or len(nums1) == 0, return an empty list?
 - The arrays aren't in increasing order, but are there guaranteed peaks in each?
 - How do I know that I've checked a number already? Or does that matter?
 - Is the nums1 list always smaller than length than nums2? No
      - I could check this be seeing if nums1 length is less than nums2 length
      - If it is, then we can stop iterating through nums2 when we've looked at elements in nums1 and vice versa
      - Suggestion:
   - Do this before searching, and pass the smaller list first as the iterator
 - Is the list increasing? To know this, I need to check left/right neighbors
      - Make sure to check that mid > 0 to not go out of bounds on the left side, and mid <= len(nums1 or nums2) - 1
      - Below assumes nums1.length < nums2.length, logic would be reversed w/this
   - if nums1 is increasing and nums2[i] > nums1[i]: reduce search space by moving nums2 to the right via right -= mid
   - if nums1 is increasing and nums2[i] < nums[i]: reduce search space by moving nums2 to the left
 - if nums1[mid] == nums2[mid]: results.append(nums1[mid]) and continue to move
 - There should probably be two sets of pointers, one set to track the location of nums1 and one to track nums2
 - I know I want to use template 1 or 2 for binary search, which requires post-processing
 - There can be multiple peaks in either array
   - peak == nums[mid - 1] > nums[mid] < nums[mid + 1]
   - Should the first check be for a peak? then search left and right?