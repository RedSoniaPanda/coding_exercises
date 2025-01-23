# [Problem Link](https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/)

# Problem Constraints
 - 1 <= num <= 2**31 - 1
 - Perfect square: int that's the square of an integer. It's the product of some int w/in itself.
 - Example: 2**2 = 4, 4 would be the input and we'd return True
 - Example: 14 is not a perfect square, because 3.742 is not an int

# Intuition
 - if num <= 2, then it's a perfect square, just return True, potential stop condition
 - The highest number that can be assessed can't be more than half of the num passed in, potential right
 - The lowest number can be 3, potential left
 - In each iteration check if the mid-point is equal to the num
   - if mid-point isn't equal, the check if the left side squared is lower than the mid-point, use mid to reduce search space on the right side right = mid - 1
   - if mid-point isn't equal, and squared left side is higher, reduce search space on the left, left = mid + 1
