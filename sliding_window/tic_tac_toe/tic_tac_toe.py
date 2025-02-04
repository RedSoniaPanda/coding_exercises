from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        pass


def test_case_1():
    actual = Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
    assert actual == "A"


if __name__ == "__main__":
    test_case_1()
