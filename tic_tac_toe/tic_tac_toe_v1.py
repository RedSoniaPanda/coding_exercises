from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        # Create a new board each time this is initialized with n x n being the parameters
        self.board = defaultdict(int)
        self.board_size = n
        self.create_tic_tac_toe_board(n)

    def create_tic_tac_toe_board(self, n: int) -> None:
        for i in range(n):
            for j in range(n):
                self.board[(i, j)] = 0

    def check_horizontal_winner(self, player: int) -> int:
        for i in range(self.board_size):
            is_player_winner_ct = 0
            for j in range(self.board_size):
                if self.board[(i, j)] == player:
                    is_player_winner_ct += 1
                else:
                    break
            if is_player_winner_ct == self.board_size:
                return player
        return 0

    def check_vertical_winner(self, player: int) -> int:
        for i in range(self.board_size):
            is_player_winner_ct = 0
            for j in range(self.board_size):
                if self.board[(j, i)] == player:
                    is_player_winner_ct += 1
                else:
                    break
            if is_player_winner_ct == self.board_size:
                return player
        return 0

    def check_diagonal_winner(self, player: int) -> int:
        is_player_winner_ct = 0
        for i in range(self.board_size):
            if self.board[(i, i)] == player:
                is_player_winner_ct += 1
        if is_player_winner_ct == self.board_size:
            return player
        for i in range(self.board_size, -1, -1):
            for j in range(0, self.board_size):
                if self.board[(j, i)] == player:
                    is_player_winner_ct += 1
        if is_player_winner_ct == self.board_size:
            return player
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        """ row is the row number and col is the column number that the player is moving to

        :param row:
        :param col:
        :param player:
        :return:
            0 - if there's no winner after the move.
            1 - if player 1 wins after the move.
            2 - if player 2 wins after the move.
        """
        if self.board[(row, col)] == 0:
            self.board[(row, col)] = player
        if self.check_diagonal_winner(player) != 0:
            print("Diagonal winner")
            return player
        if self.check_vertical_winner(player) != 0:
            print("Vertical winner")
            return player
        if self.check_horizontal_winner(player) != 0:
            print("Horizontal winner")
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

if __name__ == "__main__":
    tic_tac_toe = TicTacToe(3)  # This means 3 x 3 board and returns null
    # tic_tac_toe = TicTacToe(2)
    print(tic_tac_toe.move(0, 0, 1))  # player 1 moves on row 0 and col 0
    print(tic_tac_toe.move(0, 2, 2))
    print(tic_tac_toe.move(2, 2, 1))
    print(tic_tac_toe.move(1, 1, 2))
    print(tic_tac_toe.move(2, 0, 1))
    print(tic_tac_toe.move(1, 0, 2))
    print(tic_tac_toe.move(2, 1, 1))
    # Vertical winnner
    # tic_tac_toe.move(1, 0, 1)
    # tic_tac_toe.move(2, 0, 1)

    # Horizontal winner
    # print(tic_tac_toe.move(0, 1, 1))  # player 1 moves on row 0 and col 0
    # print(tic_tac_toe.move(0, 2, 1))  # player 1 moves on row 0 and col 0
