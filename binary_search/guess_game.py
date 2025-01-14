
def guess(num: int)->int:
    pick = 6
    if num > pick:
        return -1
    if num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            guess_res = guess(mid)
            if guess_res == -1:
                right = mid - 1
            elif guess_res == 1:
                left = mid + 1
            else:
                return mid
        return right


def test_case_1():
    num = 10
    sol = Solution()
    actual = sol.guessNumber(num)
    print(actual)
    assert actual == 6


if __name__ == '__main__':
    test_case_1()
