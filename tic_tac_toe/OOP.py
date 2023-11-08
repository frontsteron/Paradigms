class tic_tac_toe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Двумерный массив для доски 3x3
        self.current_player = "X"

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "X" if self.current_player == "O" else "O"
        else:
            print("Недопустимый ход. Попробуйте снова.")

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]
        if " " not in self.board:
            return "Ничья"
        return None

    def play(self):
        while True:
            self.print_board()
            position = int(input(f"Ход игрока {self.current_player}. Введите номер ячейки (0-8): "))
            if 0 <= position <= 8:
                self.make_move(position)
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == "Ничья":
                        print("Ничья!")
                    else:
                        print(f"Игрок {winner} выиграл!")
                    break
            else:
                print("Недопустимый ход. Введите число от 0 до 8.")


if __name__ == "__main__":
    game = tic_tac_toe()
    game.play()