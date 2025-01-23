# See writeup.md for more on the solution

class Solution:
    def pow(self, x: float, n: int):
        if n == 0: return 1
        # Make n positive and iterate until we hit n == 0
        if n < 0: return 1 / self.pow(x, -n)
        return x * self.pow(x, n-1)

    def myPow(self, x: float, n: int) -> float:
        return self.pow(x, n)


def test_case_1():
    sol = Solution()
    actual = sol.myPow(x=2.00000, n=10)
    assert actual == 1024.00000


if __name__ == "__main__":
    test_case_1()
