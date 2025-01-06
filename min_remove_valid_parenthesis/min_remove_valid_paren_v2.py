class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def minRemoveToMakeValid(self, s: str) -> str:
        # it's an empty string
        # contains only lowercase letters
        # open parenthesis must have closing parenthesis
        final_string = ""
        open_parenthesis = []
        list_length = 0
        for char in s:
            char_node = Node(char)
            if char == "(":
                open_parenthesis.append(char_node)
            elif char == ")":
                if open_parenthesis:
                    open_parenthesis.pop()
                else:
                    continue
            if self.head is None:
                self.head = char_node
                self.head.next = self.tail
                self.head.prev = self.tail
                list_length += 1
            elif self.tail is None:
                self.tail = char_node
                self.head.next = self.tail
                self.head.prev = self.tail
                self.tail.prev = self.head
                self.tail.next = self.head
                list_length += 1
            else:
                node = char_node
                temp_tail = self.tail
                self.tail = node
                temp_tail.next = self.tail
                self.tail.prev = temp_tail
                self.tail.next = self.head
                self.head.prev = self.tail
                list_length += 1
        if len(open_parenthesis) == list_length or self.head is None:
            return ""

        print_all(self.head, self.tail)
        curr_node = self.head
        while curr_node != self.tail:
            final_string += curr_node.val
            curr_node = curr_node.next
        final_string += self.tail.val
        return final_string


def print_all(head, tail):
    curr = head
    while curr != tail:
        print(curr.val)
        curr = curr.next
    if tail is not None:
        print(tail.val)
    print()


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
    test_case_2()
    # test_case_3()
    # test_case_4()
    # test_case_5()
