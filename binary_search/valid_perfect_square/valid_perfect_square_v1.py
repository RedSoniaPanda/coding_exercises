class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 2:
            return True

        l, r = 2, num // 2
        while l <= r:
            mid = (l + r) // 2
            mid_sq = mid * mid
            if mid_sq == num:
                return True

            if num > mid_sq:
                l = mid + 1
            else:
                r = mid - 1
        return False


def test_case_1():
    sol = Solution()
    actual = sol.isPerfectSquare(16)
    assert actual == True


def test_case_2():
    sol = Solution()
    actual = sol.isPerfectSquare(2)
    assert actual == True


if __name__ == "__main__":
    test_case_1()
    test_case_2()
