from menu.menu_select import header

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

currentPlayer = 'X'
winner = None
gameRunning = True


def tic_tac_play():
    header('Bem vindo ao jogo da Velha')

    def print_board(board):
        print(board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('---------')
        print(board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('---------')
        print(board[0] + ' | ' + board[1] + ' | ' + board[2])

    def player_input(board):
        inp = int(input('Insira um número ente 1-9: '))
        if 1 <= inp <= 9 and board[inp - 1] == '-':
            board[inp - 1] = currentPlayer
        else:
            print('Esse espaço já está preenchido')

    def check_horizontle(board):
        global winner
        if board[0] == board[1] == board[2] and board[1] != '-':
            winner = board[0]
            return True
        elif board[6] == board[4] == board[2] and board[2] != '-':
            winner = board[2]
            return True

    def check_row(board):
        global winner
        if board[0] == board[3] == board[6] and board[0] != '-':
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != '-':
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != '-':
            winner = board[2]
            return True

    def check_diagonal(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != '-':
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != '-':
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != '-':
            winner = board[6]
            return True

    def check_tie(board):
        global gameRunning
        if '-' not in board:
            print_board(board)
            print('Deu velha!')
            gameRunning = False

    def check_win():
        global gameRunning
        if check_diagonal(board) or check_horizontle(board) or check_row(board):
            print(f'O vencedor é o {winner}')
            print_board(board)
            gameRunning = False

    def switch_player():
        global currentPlayer
        if currentPlayer == 'X':
            currentPlayer = '0'
        else:
            currentPlayer = 'X'

    while gameRunning:
        print_board(board)
        player_input(board)
        check_win()
        check_tie(board)
        switch_player()


if __name__ == '__main__':
    tic_tac_play()
