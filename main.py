class TicTacToe:
    board = []
    turn = 'X'

    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        while True:
            if self.player_turn() == 'X':
                self.x_move()
            else:
                self.o_move()

            self.show_board()
            if self.check_winner():
                break

    def x_move(self):
        move = input('X cell (row col)\n')
        i, j = move.split(' ')

        cell = self.board[int(i) - 1][int(j) - 1]

        if cell:
            print('This cell is not empty')
            self.x_move()
            return

        # self.show_board()
        self.board[int(i) - 1][int(j) - 1] = 'X'

    def o_move(self):
        move = input('O cell (row, col)\n')
        i, j = move.split(' ')

        cell = self.board[int(i) - 1][int(j) - 1]

        if cell:
            print('This cell is not empty')
            self.o_move()
            return

        self.board[int(i) - 1][int(j) - 1] = 'O'

    def show_board(self):
        for row in self.board:
            print(row)

    def check_winner(self):
        for i in self.board:
            if i[0] and i[0] == i[1]:
                if i[1] == i[2]:
                    print('X won'.format(i[0]))
                    return True

        for j in range(3):
            if self.board[0][j] and self.board[0][j] == self.board[1][j]:
                if self.board[1][j] == self.board[2][j]:
                    print('{} won'.format(self.board[0][j]))
                    return True

        if self.board[0][0] and self.board[0][0] == self.board[1][1]:
            if self.board[1][1] == self.board[2][2]:
                print('{} won'.format(self.board[1][1]))
                return True

        if self.board[0][2] and self.board[0][2] == self.board[1][1]:
            if self.board[1][1] == self.board[2][0]:
                print('{} won'.format(self.board[1][1]))
                return True

        for row in self.board:
            if not all(row):
                return

        print('No winner')

    def player_turn(self):
        current_turn = self.turn
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

        return current_turn


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = TicTacToe()
