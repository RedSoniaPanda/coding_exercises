from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.w_list = w
        # Probability of a num being selected once
        # probability = 1 / sum(self.w_list)
        self.prob = 1 / sum(self.w_list)
        self.picks = []

    def pickIndex(self) -> int:
        if len(self.w_list) == 1:
            # Always return 0 if there's only one element in the list
            return 0
        # How do I know which way to go? after finding midpoint?
        mid_point = len(self.w_list) // 2  # mid point
        # Range [0, len(self.w_list) - 1]
        left = 0
        right = len(self.w_list) - 1
        if len(self.picks) == 0:
            # self.picks.append()
            pass

        return 0


def test_case_2():
    w = [1, 3]
    sol = Solution(w)
    picks = []
    for i in range(6):
        picks.append(sol.pickIndex())
    assert 0 in picks
    assert 1 in picks


def test_case_1():
    w = [1]
    sol = Solution(w)
    assert sol.pickIndex() == 0


if __name__ == '__main__':
    test_case_1()
    test_case_2()