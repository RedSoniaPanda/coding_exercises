from typing import List


class Solution:
    def __init__(self):
        self.len_code = -1

    def replace_k_next_nums(self, code, k) -> List[int]:
        new_code = []

        for n in range(len(code)):
            sum_k_next = 0
            for i in range(1, k+1):
                next_index = n + i
                if next_index > self.len_code:
                    next_index = ((n + i) - self.len_code) - 1
                sum_k_next += code[next_index]
            new_code.append(sum_k_next)
        return new_code

    def replace_k_prev_nums(self, code, k) -> List[int]:
        new_code = []

        for n in range(len(code)):
            sum_k_prev = 0
            for i in range(n - 1, (k + n) - 1, -1):
                prev_index = i
                sum_k_prev += code[prev_index]
            new_code.append(sum_k_prev)
        return new_code

    def decrypt(self, code: List[int], k: int) -> List[int]:
        self.len_code = len(code) - 1
        if k > 0:
            return self.replace_k_next_nums(code, k)
        elif k < 0:
            return self.replace_k_prev_nums(code, k)
        else:
            return [0] * len(code)


def test_case_1():
    # k == 0
    code = [5, 7, 1, 4]
    k = 0

    sol = Solution()
    actual = sol.decrypt(code, k)
    assert actual == [0, 0, 0, 0]


def test_case_2():
    # k > 0
    code = [5, 7, 1, 4]
    k = 3

    sol = Solution()
    actual = sol.decrypt(code, k)
    assert actual == [12,10,16,13]


def test_case_3():
    # k < 0
    code = [2,4,9,3]
    k = -2

    sol = Solution()
    actual = sol.decrypt(code, k)
    assert actual == [12,5,6,13]


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
