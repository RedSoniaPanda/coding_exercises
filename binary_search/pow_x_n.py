# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # The iterative way would be using n as the range and
        # multiplying it by itself for each n

        # Rules of the problem:
        #    - n is an integer
        #    - Either x is not zero or n > 0
        #    - -10**4 <= x**n <= 10**4
        if x == 0.0:
            # if x equals 0 then n cannot be negative, so just return 0
            return 0

        # Another exp rule
        if n == 0 and x > 0:
            return 1
        elif n == 0 and x < 0:
            return -1

        # Left bound is as far neg as we can go w/output
        # l = -10**4 if x < 0 else 0
        # right bound is as far pos as we can go w/output
        # r = 10**4 if x > 0 else 0

        # can I use the dynamic range finder to get the right answer?
        # how do I know if I've reached the end? - iteratively, when n == 0, so it should be the
        # same here
        # I can repeatedly square the number and then half n
        # x**n == x*(x**n)
        # Mathematically, (x**2)**(n/2) if x is even, x*(x**2)**((n-1)/2) if x is odd
        result = 0
        # Change n to a positive number and then change the result at the end to be the recipricol
        if n < 0:
            is_neg = True
            n = -1 * n
        else:
            is_neg = False
        # TODO Come back at some point! The solution here is not correct
        while n != 0:
            if n % 2 == 0:
                result += (x * x)**(n / 2)
                n = n / 2
            else:
                result += x*(x * x)**((n - 1) / 2)
                n = (n - 1) / 2

        if is_neg:
            result =- result

        return result


def test_case_1():
    sol = Solution()
    actual = sol.myPow(1, 0)
    expected = 1.0
    assert actual == expected


def test_case_2():
    sol = Solution()
    actual = sol.myPow(-1, 0)
    expected = -1.0
    assert actual == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
