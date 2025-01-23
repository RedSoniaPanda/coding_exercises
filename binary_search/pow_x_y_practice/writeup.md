 # [Problem Link](https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/)

# Intuition
The iterative way would be using n as the range and multiplying it by itself for each n, stopping at 0
how do I know if I've reached the end? - iteratively, when n == 0
  - Left bound is as far neg as we can go w/output
  - l = -10**4 if x < 0 else 0
  - right bound is as far pos as we can go w/output
  - r = 10**4 if x > 0 else 0

can I use the dynamic range finder to get the right answer? - Not needed, the answer relies on exponential rules
which can then be paired w/recursion

# Rules of the problem:
 - n is an integer
 - Either x != 0 or n > 0
 - -10**4 <= x**n <= 10**4
 - -100.0 < x < 100.0

# Some math rules:
 - x**0 == 1 if pos, or -1 if neg, n == 0
 - If x == 0, then result will be 0 because n has to be greater than 0 when x == 0
 - Neg exponent rule x**-n == (1/(x**n))
 - pos exponent rule where n < 0, x**n == (1/(x**(-1*n)))
 - for any n > 1 x**n == x * x**(n-1)

# Before the binary search, make n positive if it's negative
if n is negative, we should also make x = 1/x

# For the binary search:
 - if n reaches 0, we've hit the end
 - compute x * x**n-1 by using recursion
 - Decrease n by 1 if we use the simpler recursive method
 - Otherwise, decrease the search space by dividing n in half and multiplying x
 - (x**2)**(n/2) if x is even, x*(x**2)**((n-1)/2) if x is odd
 - x**n == x*(x**-n)