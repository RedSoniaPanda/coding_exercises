class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars_in_s = []
        open_parenthesis = []
        final_string_index = 0
        for char in s:
            if char == "(":
                open_parenthesis.append(final_string_index)
            elif char == ")" and open_parenthesis:
                open_parenthesis.pop()
            elif char == ")":
                continue
            chars_in_s.append(char)
            final_string_index += 1

        final_string = []
        if open_parenthesis:
            for index in range(len(open_parenthesis)):
                if index == 0:
                    for i in range(open_parenthesis[index]):
                        final_string.append(chars_in_s[i])
                else:
                    for i in range(open_parenthesis[index - 1] + 1, open_parenthesis[index]):
                        final_string.append(chars_in_s[i])
            final_string = "".join(final_string)
        else:
            final_string = "".join(chars_in_s)
        return final_string


def test_case_1():
    sol = Solution()
    s = "lee(t(c)o)de)"
    expected_output = "lee(t(c)o)de"
    actual_output = sol.minRemoveToMakeValid(s)
    print(actual_output)
    assert actual_output == expected_output


def test_case_2():
    sol = Solution()
    s = "))(("
    expected_output = ""
    actual_output = sol.minRemoveToMakeValid(s)
    print(actual_output)
    assert actual_output == expected_output


def test_case_3():
    sol = Solution()
    s = "a)b(c)d"
    expected_output = "ab(c)d"
    actual_output = sol.minRemoveToMakeValid(s)
    print(actual_output)
    assert actual_output == expected_output


def test_case_4():
    sol = Solution()
    s = "(a(b(c)d)"
    expected_output = "a(b(c)d)"
    actual_output = sol.minRemoveToMakeValid(s)
    print(actual_output)
    assert actual_output == expected_output


def test_case_5():
    sol = Solution()
    s = "())()((("
    expected_output = "()()"
    actual_output = sol.minRemoveToMakeValid(s)
    print(actual_output)
    assert actual_output == expected_output


if __name__ == '__main__':
    # test_case_1()
    # test_case_2()
    # test_case_3()
    test_case_4()
    test_case_5()
