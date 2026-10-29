# 36th github project --> Tic-Tac-Toe
print('----------Tic-Tac-Toe---------')
board = [" "] * 9


def show_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")


def winner():
    lines = [(0,1,2), (3,4,5), (6,7,8),
             (0,3,6), (1,4,7), (2,5,8),
             (0,4,8), (2,4,6)]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, pick 1-9: ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            print("Invalid or taken.")
        except ValueError:
            print("Enter a number 1-9.")


def main():
    print("TIC-TAC-TOE")
    player = "X"
    moves = 0

    while moves < 9:
        show_board()
        board[get_move(player)] = player
        moves += 1

        win = winner()
        if win:
            show_board()
            print(f"Player {win} wins!")
            return

        player = "O" if player == "X" else "X"

    show_board()
    print("It's a draw!")



main()