

class Solution:
    def __init__(self):
        self.open_brackets = ["(", "[", "{"]
        self.close_brackets = [")", "]", "}"]
        self.bracket_map = {"(": ")", "[": "]", "{" : "}"}

    def isValid(self, s: str) -> bool:
        exist_open_brackets = []
        exist_close_brackets = []
        for char in s:
            if char in self.open_brackets:
                exist_open_brackets.append(char)
            if char in self.close_brackets:
                exist_close_brackets.append(char)

        # print(exist_open_brackets)
        # print(exist_close_brackets)
        if len(exist_open_brackets) != len(exist_close_brackets):
            return False

        is_back_to_back = True
        for i in range(len(exist_open_brackets)):
            if self.bracket_map[exist_open_brackets[i]] != exist_close_brackets[i]:
                is_back_to_back = Falsevalid_parenthesis_v1_solution_doesnt_work.py
        if not is_back_to_back:
            # Parse differently
            for i in range(len(exist_open_brackets)):
                close_val = exist_close_brackets[len(exist_close_brackets) - 1 - i]
                if self.bracket_map[exist_open_brackets[i]] != close_val:
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
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    test_case_5()
