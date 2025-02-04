# Chat Gpt Discussions

_**Question**: Can you give me some tips on how to approach solving a sliding window problem?_ 

## Takeaways

 - Look for the words contiguous subarray/subsequence of a given arr/str
   - Working w/problems including: sums, products, maxs, mins, or counts w/in a subarray
   - Involves constraints like "at most k elements", "subarray of size k", or "within a certain range"
 - Slide a window, to save compute time
 - Three forms:
   - Fixed: Window size is constant
     - Example: find max sum of subarray of size k
   - Variable: Window size can expand/shrink dynamically
     - Example: Find smallest subarray w/a sum >= target
   - Two-pointer: Used when there are two conditions
     - Example: Longest substring with at most k distinct characters
 - I put the steps to solving a problem in the sub-folder readmes of this project, which differs per problem constraints
   - Generic steps are:
     - maintain the window size/constraints
     - efficiently update intermediate results
     - know when to expand/shrink the window
 - Frequency Map: For problems involving characters or distinct elements, a frequency map (dictionary in Python) can help you track counts efficiently.
 - Use a running sum, product, or other intermediate results to avoid recomputing values for the entire window.
 - Consider edge cases like empty arrays, single-element arrays, or when constraints (like k) are very large or small.
 - If the problem involves two different conditions, you might need two pointers moving independently.
