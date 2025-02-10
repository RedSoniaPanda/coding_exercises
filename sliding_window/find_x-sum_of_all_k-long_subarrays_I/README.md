# [Problem Link](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/)

# Constraints

 - 1 <= n == nums.length <= 50
 - 1 <= nums[i] <= 50
 - 1 <= x <= k <= nums.length

# Intuition

 - k is the first window
 - Then I should figure out the frequency of each num in that subarray
   - Preferably put in descending order of frequency, so that the next part can just be the first x numbers in that set
   - One way is to increase the frequency count for the number and then check if it's greater than or equal to the current max frequency
     - If it already exists in the set, it should be removed and added to the front
     - Otherwise just add to the front
     - if it's equal to the frequency, then check the number for the max frequency and if it's larger then move to the front of the list
     - Otherwise add after
 - Then take the x number of frequent nums to sum
