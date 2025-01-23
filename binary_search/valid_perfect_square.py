# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # A perfect square has to be even on all sides
        # 1 <= num <= 2**31 - 1
        # is_odd = True if num % 2 == 0 else False
        # while num != 0
        if num < 2:
            return True
        l = 2  # Can't ever be 0 because 0**2 == 0, but also should be at least two, or return above
        r = num // 2 # the square won't be over half
        while l <= r:
            mid = l + (r - l) // 2
            val = mid * mid
            if val == num:
                # TODO Need to check for a remainder here!! Actually may not have to
                return True

            if val > num:
                r = mid - 1
            else:
                l = mid + 1
        return False


def test_case_1():
    sol = Solution()
    num = 1
    actual = sol.isPerfectSquare(num)
    assert actual == True


def test_case_2():
    sol = Solution()
    num = 2
    actual = sol.isPerfectSquare(num)
    assert actual == False


def test_case_3():
    sol = Solution()
    num = 16
    actual = sol.isPerfectSquare(num)
    assert actual == True


def test_case_4():
    sol = Solution()
    num = 3
    actual = sol.isPerfectSquare(num)
    assert actual == False


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
