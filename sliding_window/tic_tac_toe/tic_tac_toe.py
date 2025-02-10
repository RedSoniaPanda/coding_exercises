from typing import List


class Solution:
    def __init__(self):
        self.player_a_rows = [0] * 3
        self.player_a_cols = [0] * 3
        self.player_b_rows = [0] * 3
        self.player_b_cols = [0] * 3
        self.size = 3
        # self.player_a = {"row 1": [1], "row 2": [1, 2]

    # def _check_diag(self, start, end):
    #     diag_ct = 0
    #     while start + 1 <= end:
    #         start_val = self.player_a[start][0]
    #         if abs(self.player_a[start][0] - self.player_a[start + 1][0]) == abs(self.player_a[start][1] - self.player_a[start + 1][1]):
    #             diag_ct += 1
    #         start += 1
    #     if abs(self.player_a[end][0] - self.player_a[end - 1][0]) == abs(self.player_a[end][1] - self.player_a[end - 1][1]):
    #         diag_ct += 1
    #     return diag_ct

    # def _check_horizontal(self, start, end):
    #     horizon_ct = 0
    #     while start + 1 <= end:
    #         if self.player_a[start][0] == self.player_a[start + 1][0]:
    #             horizon_ct += 1
    #         start += 1
    #     if self.player_a[end][0] == self.player_a[end - 1][0]:
    #         horizon_ct += 1
    #     return horizon_ct

    # def _check_vertical(self, start, end):
    #     vertical_ct = 0
    #     while start + 1 <= end:
    #         if self.player_a[start][1] == self.player_a[start + 1][1]:
    #             vertical_ct += 1
    #         start += 1
    #     if self.player_a[end][1] == self.player_a[end - 1][1]:
    #         vertical_ct += 1
    #     return vertical_ct
    #
    # def check_winner_a(self, start: int, end: int) -> bool:
    #     if self._check_diag(start, end) == self.size:
    #         return True
    #     if self._check_horizontal(start, end) == self.size:
    #         return True
    #     if self._check_vertical(start, end) == self.size:
    #         return True
    #     return False

# in_i = self.player_a[start][0]
    # in_y = self.player_a[start][1]
    # in2_i = self.player_a[end][0]
    # in2_y = self.player_a[end][1]
    # # Check for diagonal winner
    # if abs(in_i - in2_i) == abs(in_y - in2_y):
    #     is_winner = True
    # elif in_i == in2_i:
    #     is_winner = True
    # elif in_y == in2_y:
    #     is_winner = True
    # return is_winner

    def tictactoe(self, moves: List[List[int]]) -> str:
        result = "pending"
        if len(moves) < 5:
            return result

        # Check player A wins first
        pa_winner = False
        for p_a in range(0, 5, 2):
            self.player_a_rows[moves[p_a][0]] += 1
            self.player_a_cols[moves[p_a][1]] += 1
            if p_a == 4:
                start = 0
                end = 2
                pa_winner = self.check_winner_a(start, end)
        if pa_winner:
            return "A"

        start = 4
        n = len(moves)
        # for p_a in range(start, n, 2):
        #     row = moves[p_a][0]
        #     col = moves[p_a][1]

        return result


def test_case_1():
    actual = Solution().tictactoe([[0,0],[2,0],[1,1],[2,1]])
    assert actual == "pending"


def test_case_2():
    # Diagonal win player A
    actual = Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
    assert actual == "A"


def test_case_3():
    # Horizontal win player A
    actual = Solution().tictactoe([[0,0],[2,0],[0,1],[2,1],[0,2]])
    assert actual == "A"


def test_case_4():
    # Vertical win player A
    actual = Solution().tictactoe([[0,0],[2,0],[1,0],[2,1],[2,0]])
    assert actual == "A"


def test_case_5():
    actual = Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,0]])
    assert actual == "pending"


if __name__ == "__main__":
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    test_case_5()
