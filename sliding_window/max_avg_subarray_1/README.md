[Problem Link](https://leetcode.com/problems/maximum-average-subarray-i/)

# Constraints

 - n == nums.length
 - 1 <= k <= n <= 105
 - -104 <= nums[i] <= 104

# Intuition
 - Continuous subarray means that 1,12,-5 != 1,-5
 - Also screams binary search, maybe a combo?
 - For sliding window
   - window size is fixed at k
   - the array's not circular, so if the current position + k > len(input), we're done searching
 - What if k > size of input? Return -1? It's not possible to have a value k larger than the array size!
 - r_sum = sum(input[0:k-1]), start=0, end = k - 1

# Pseudocode

```
max_sum = 0
running_sum = 0
for i in range(k):
    max_sum += input[i]

for i in range(len(input)):
    sum += input[i] - input[i - k]
    max_sum = max(max_sum, sum)

return max_sum / k
```
