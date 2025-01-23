from typing import List

"""
l = 0
r = len(letters) - 1
target_ord = ord(target)
if target == "z" or target == letters[r] or target_ord > ord(letters[r]):
    return letters[0]
# result = letters[0]
result = letters[r]
while l <= r:
    mid = (l + r) // 2
    result_ord = ord(result)
    mid_ord = ord(letters[mid])
    if result_ord == target_ord:
        result = letters[mid]
    elif mid_ord > target_ord and abs(mid_ord - target_ord) < abs(target_ord - result_ord):
        result = letters[mid]

    if ord(letters[l]) < target_ord:
        l = mid + 1
    else:
        r = mid - 1

return result"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """ Letters and target will ALWAYS be lowercase
        Length of letters will always be  2 <= length <= 10**4
        Letters contains at least 2 diff characters
        Should I first find the target's diff from a?
        """
        if target == "z" or target >= letters[-1]:
            return letters[0]

        l, r = 0,len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                # Str comparison can just be a < c
                l = mid + 1
            else:
                r = mid - 1
        if l == len(letters):
            return letters[0]
        else:
            return letters[l]


def test_case_1():
    sol = Solution()
    letters = ["x", "x", "y", "y"]
    actual = sol.nextGreatestLetter(letters, 'z')
    assert actual == 'x'


def test_case_2():
    sol = Solution()
    letters = ["a", "b", "c"]
    actual = sol.nextGreatestLetter(letters, 'd')
    assert actual == 'a'


def test_case_3():
    sol = Solution()
    letters = ["c", "f", "j"]
    actual = sol.nextGreatestLetter(letters, 'c')
    assert actual == 'f'


def test_case_4():
    sol = Solution()
    letters = ["c", "f", "j"]
    actual = sol.nextGreatestLetter(letters, 'a')
    assert actual == 'c'


def test_case_5():
    sol = Solution()
    letters = ["c", "f", "j"]
    actual = sol.nextGreatestLetter(letters, 'd')
    assert actual == 'f'



if __name__ == "__main__":
    test_case_1()
    test_case_2()
    # test_case_3()
    # test_case_4()
    # test_case_5()
