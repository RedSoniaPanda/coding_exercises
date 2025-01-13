# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/

def isBadVersion(n):
    if n >= 4:
        return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left != right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # Has to be lower
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    input = [5, 4]
    sol = Solution()
    for i in input:
        assert sol.firstBadVersion(i) == 4
