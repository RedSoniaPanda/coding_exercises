class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = len(s)
        if end == 0:
            return 0
        elif end == 1:
            return 1

        max_len = -1
        final_str = set()
        start = 0
        while start != end:
            for c in range(start, end):
                if s[c] not in final_str:
                    final_str.add(s[c])
                else:
                    max_len = max(len(final_str), max_len)
                    final_str = set()
                    break
            start += 1
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
