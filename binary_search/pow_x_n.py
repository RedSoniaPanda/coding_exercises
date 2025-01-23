# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/
# See pow_x_y_practice\writeup.md for more on the solution

class Solution:
    # There are two optimal solutions here, both use recursion!
    def pow_1(self, x: float, n: int) -> float:
        # this solution is the most optimal because it divides the search space in half
        if n == 0: return 1
        if n < 0: return 1 / self.pow_1(x, -n)

        if n % 2 == 0: return self.pow_1(x * x, n // 2)
        else: return x * self.pow_1(x * x, (n - 1) // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.pow_1(x, n)


def test_case_1():
    sol = Solution()
    actual = sol.myPow(1, 0)
    expected = 1.0
    assert actual == expected


def test_case_2():
    sol = Solution()
    actual = sol.myPow(-1, 0)
    expected = 1
    assert actual == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
