from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k == 0:
            return result

        n = len(code) - 1
        if k > 0:
            start = 1  # Starts at 1 because we don't include the initial value
            end = k
        else:
            start = len(code) - abs(k)
            end = n

        sum = 0
        n = len(code)
        for i in range(start, end + 1):
            sum += code[i]
        for i in range(n):
            result[i] = sum
            # Modulo is required here to make sure that we don't go out of bounds
            sum -= code[start % n]  # This is for circular arrays, if this wasn't circular, we'd not include this and instead add bounds checkers
            sum += code[(end + 1) % n]
            start += 1
            end += 1
        return result


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
    print(actual)
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