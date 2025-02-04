class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        max_len = -1

        start = 0
        final_str = {}
        for end in range(n):
            if s[end] in final_str:
                # Recalculate the start point!
                start = max(final_str[s[end]], start)

            # take the index of the end point, and subtract the start point,
            # add one, and you have the diff in length
            max_len = max(max_len, end - start + 1)
            # reset the index for the char we're currently evaluating
            final_str[s[end]] = end + 1
        return max_len


def test_case_1():
    sol = Solution()
    length = sol.lengthOfLongestSubstring("au")
    assert length == 2
    length = sol.lengthOfLongestSubstring("abcabcbb")
    assert length == 3
    length = sol.lengthOfLongestSubstring("aa")
    assert length == 1
    length = sol.lengthOfLongestSubstring("")
    assert length == 0
    length = sol.lengthOfLongestSubstring("a")
    assert length == 1
    length = sol.lengthOfLongestSubstring("anviaj")
    assert length == 5


if __name__ == "__main__":
    test_case_1()
