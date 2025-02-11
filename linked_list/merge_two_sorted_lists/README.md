[Problem Link](https://leetcode.com/problems/merge-two-sorted-lists/description/)

# Constraints

 - The number of nodes in both lists is in the range [0, 50].
 - -100 <= Node.val <= 100
 - Both list1 and list2 are sorted in non-decreasing order.

# Intuition

 - The lists are sorted
 - The two lists don't have to be the same size, I have to know which is bigger and use that as the outside iterator?
 - The tricky part is the node value in list 2 could start with 40 while list 1 starts with 1
 - Should I find out which has the smallest starting point?
 - Should I figure out the max?
 - There are dupes in the final list, are there dupes in the inputs?
   - Yes! I tried this in leetcode test cases, there can be dupes in a single list
