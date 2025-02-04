# [Defuse the bomb](https://leetcode.com/problems/defuse-the-bomb/description/)

## Intuition

 - if k > 0, replace ith num w/sum of the **next** k numbers
   - Example: sum = ((i + 1) + (i + 2) + (i + 3)) if k == 3
   - start = 0, end = k
   - compute the sum of first window size sum -= array[start % len(arr)] and sum += array[(end + 1) % len(arr)] 
   - add it to the current start position
   - incr start and end by 1
 - if k < 0, replace ith num w/sum of **prev** k nums
   - Example: sum = ((i - 1) + (i - 2) + (i - 3)) if k == 3
   - k is the window length size
   - compute the sum of first window size sum -= array[start % len(arr)] and sum += array[(end + 1) % len(arr)] 
   - Then add the sum to the current start position
   - Then increase start and end by 1
   - then compute sum again by subtracting start and adding end
- if k == 0, replace ith num w/0
   - Initialize a list with all zeros, that's the size of the array
   - Use the list when calculating results for when k != 0

_deprecated_
 - If I leave the input as an array of ints, then calculating the index of the numbers we want to sum will require some checks
   - i - x < 0
     - Maybe I can just calculate the diff of i - x?
   - i + x > len(arr) - 1
     - ((i + x) - (len(arr) - 1)) - 1
     - I think this equation should get us back from the beginning

# Solution Notes - in defuse_bomb_v2.py
 - Sliding window technique: the modulo should be used w/start and end points
   - Step 1 is to calculate the sum of the current range, which is going to be 1 to k if k is positive
     - Step 1: Think of starting at 0, and k = -2. If the array is len 4 then the start point is the third spot and the end is the last spot
       - This means we can calculate the start point from 0 being len(array) - abs(k) and the end will be the end of the list
   - Step 2 is to iterate through the len(array)
     - store the sum first
     - then subtract the start % n
     - Followed by adding the (end + 1) % n
     - Then increase both the start and end points
