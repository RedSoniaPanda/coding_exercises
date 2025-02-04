# [Problem Link](https://leetcode.com/problems/contains-duplicate-ii/description/)

# Constraints

 - 1 <= nums.length <= 105
 - -109 <= nums[i] <= 109
 - 0 <= k <= 105

# Intuition
 - two distinct indices - This means I'm only comparing two values at once, i and j, which are indices of nums
 - One check is that nums[i] == nums[j] and abs(i - j) <= k
   - Return true as soon as this condition is met
 - This is similar to a circular list, because the indices may loop around
   - Example: len(nums) == 4, start == 3, that means that we should compare spots 0, 1, and 2. So end will need to start at 0
 - If I think iteratively, then I'd compare spot zero with spot 1, then spot zero with spot 2, until I reached spot zero with spot 3 (i.e. len(nums) - 1)
   - The number of spots to check is len(nums) - 1
   - for i in range(len(nums) - 1), for j in range(1, len(nums) - 1) These are the iterative loops
 - I could potentially split this into two problems, one is to find dupes and another is to check the abs val diff is smlr or equal to k
 - start = 1, end = len(nums) -1, for i in range(len(nums) - 1): if nums[i] == nums[start] and abs(nums[i] - nums[start]) <= k: return True
   - elif nums[i] == nums[end] and abs(nums[i] - nums[end]): return True
   - start = start % len(nums)
   - end = (end + 1) % len(nums)

# Things I missed
 - The k value is the distance from i to j

# Steps to solve sliding window problems
 1. Identify
    - what am I looking for? Two distinct indices (i, and j) such that nums[i] == nums[j] AND abs(i - j) <= k
    - Is the window size fixed, or variable? It's **fixed** because the user passes in k, which is also the distance between the two duplicate indices
    - Are there any constraints? Listed in the header Constraints
 2. Decide on window type, either fixed or variable. **Fixed**
    - w/Fixed: Use simple loop w/fixed range
 3. Initialize variables
    - Track window: start/end or a for loop. I think a for loop would be fine for fixed window
    - Store immediate results
    - keep track of the best result
 4. Slide the window
    - Expand the window by moving the end pointer
 5. Update the result, when there's a valid window
 6. Optimize: Avoid unnecessary calculations