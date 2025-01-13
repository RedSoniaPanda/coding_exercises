class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        # The square root is always smaller than x / 2
        # and larger than 0
        left = 2  # Minimum is always 2
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            fact = mid * mid
            if fact == x:
                return mid
            # The below wasn't needed because the right
            # if (mid * mid < x) and (((mid + 1) * (mid + 1)) > x):
            #     return mid
            if fact > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


def test_case_1():
    num = 16
    sol = Solution().mySqrt(num)
    assert sol == 4


def test_case_2():
    num = 32
    sol = Solution().mySqrt(num)
    assert sol == 5


if __name__ == "__main__":
    test_case_1()
    test_case_2()
