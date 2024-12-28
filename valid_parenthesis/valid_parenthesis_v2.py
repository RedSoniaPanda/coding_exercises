

class Solution:
    def __init__(self):
        self.open_brackets = ["(", "[", "{"]
        self.bracket_map = {"(": ")", "[": "]", "{" : "}"}

    def isValid(self, s: str) -> bool:
        opens = []
        for char in s:
            if char in self.open_brackets:
                opens.append(char)
            else:
                if len(opens) == 0:
                    return False
                if self.bracket_map[opens[-1]] != char:
                    return False
                else:
                    opens.pop()
        if opens:
            return False
        return True


def test_case_1():
    s = "()"
    assert Solution().isValid(s)


def test_case_2():
    s = "()[]{}"
    assert Solution().isValid(s)


def test_case_3():
    s = "(]"
    assert Solution().isValid(s) == False


def test_case_4():
    s = "([])"
    assert Solution().isValid(s)


def test_case_5():
    s = "([)]"
    assert Solution().isValid(s) == False



if __name__ == '__main__':
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
