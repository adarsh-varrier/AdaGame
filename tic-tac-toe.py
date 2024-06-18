import random

def display(board):
    print('\n' * 100)
    print('--------------')
    print('|   |   |   |')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ' )
    print('|   |   |   |')
    print('--------------')
    print('|   |   |   |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('|   |   |   |')
    print('--------------')
    print('|   |   |   |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print('|   |   |   |')
    print('--------------')

def player_Mark():
    """
    output:  (player1 marker,player2 marker)
    """
    marker=""
    while not (marker == 'X' or marker =='O'):
        marker=input("Select Any Side 'X' or 'O':-").upper()
        if (marker != 'X' and marker != 'O'):
            print("Select Either X or O!!")
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
def position_mark(board,position,marker):
    board[position] = marker
def win_check(board, mark):
    """Win Or Loss"""
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark) )
def randomselection():
    flag=random.randint(0,1)
    if flag == 0:
        return 'Player-1'
    else:
        return 'Player-2'

def space_check(board,position):
    return board[position] == ' '
def full_or_not(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    """Board is full"""
    return True
def pos_selection(board,turn,player):
    print(turn,"(",player,") is choise ")
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9): '))
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
            print("Enter number With in the Limit! OR check the selected position is already Assigned!!")

    return position
def gamestop():
    print("!!!Game Over!!!")
def play_againn():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    print("exe stopped!")
print("\n")
print('!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!! ** Welcome to Tic - Tac - Toe ** !!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!')
print("\n")
play_again = True
while play_again:
    the_board=[' '] * 10
    player1, player2 = player_Mark()
    turn=randomselection()
    print(turn," Will Play First!")
    play_game='Wrong'
    while play_game not in ['Y',"N"]:
        play_game=input("Ready to play game(Y/N):").upper()
        if play_game not in ['Y',"N"]:
            print("Enter Option 'Y' OR 'N'!")
    if play_game == 'Y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == 'Player-1':
            display(the_board)
            position = pos_selection(the_board,turn,player1)
            print("Entered pos:",position)
            position_mark(the_board, position, player1)
            if win_check(the_board,player1):
                display(the_board)
                print("player1 Has Won!!")
                gamestop()
                game_on = False
            else:
                if full_or_not(the_board):
                    display(the_board)
                    print( "ITS TIE!!")
                    gamestop()
                    game_on = False
                else:
                    turn = 'Player-2'
        else:
            display(the_board)
            position = pos_selection(the_board,turn,player2)
            position_mark(the_board, position, player2)
            if win_check(the_board,player2):
                display(the_board)
                print("player-2 Has Won!!")
                gamestop()
                game_on = False
            else:
                if full_or_not(the_board):
                    display(the_board)
                    print("ITS TIE!!")
                    game_on = False
                    gamestop()
                else:
                    turn = 'Player-1'
    if not play_againn():
        break


