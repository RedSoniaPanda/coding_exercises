class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # it's an empty string
        # contains only lowercase letters
        # open parenthesis must have closing parenthesis
        final_string = ""
        open_parenthesis = []
        for char in s:
            if char == "(":
                open_parenthesis.append(char)
            elif char == ")":
                if open_parenthesis:
                    open_parenthesis.pop()
                else:
                    continue
            final_string += char
            print(f"adding {char} to final string {final_string}")
        if open_parenthesis:
            tmp_final = ""
            for char in final_string:
                if char == "(" and len(open_parenthesis) != 0:
                    open_parenthesis.pop()
                    continue
                tmp_final += char
            # print(f"open parenthesis exist at the end {final_string} and {tmp_final}")
            final_string = tmp_final
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
    # test_case_4()
    test_case_5()
