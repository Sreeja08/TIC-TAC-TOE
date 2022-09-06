#player1 = input("Please pick a marker 'X' or 'O': ")
#print('\n'*100)
def display_board(board):
    print('  |   |')
    print('' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print('' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print('' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('  |   |')
    print('-----------')

test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 : Do you want to be 'X' or 'O'").upper()

        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

#print(player_input())

def place_marker(board,marker,position):
    board[position] = marker

#place_marker(test_board,'@',7)
#place_marker(test_board,'$',9)
#display_board(test_board)

def win_check(board,mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[7] == mark and board[4] == mark and board[1] == mark) or
           (board[8] == mark and board[5] == mark and board[2] == mark) or
           (board[9] == mark and board[6] == mark and board[3] == mark) or
           (board[7] == mark and board[5] == mark and board[3] == mark) or
           (board[9] == mark and board[5] == mark and board[1] == mark))

#print(win_check(test_board,"X"))

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player2'
    else:
        return 'Player1'

#print(choose_first())

def space_check(board,position):
    return board[position] == ' '

#print(space_check(test_board,9))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#print(full_board_check(test_board))

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter your next position (1-9): "))
    return position

#print(player_choice(test_board))

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

######################################

print("Welcome to TIC-TAC-TOE!!")

while True:
    #rest the board
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Are you ready to play? Enter Yes or No.")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #player1 turn
        if turn == "player 1":
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print("Congratulations! player1 have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a Draw!!")
                    break
                else:
                    turn = 'player 2'

        else:
            #player2 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print("Congratulations! player2 have won the game!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a Draw!!")
                    break
                else:
                    turn = 'player 1'

    if not replay():
        break







