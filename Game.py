from IPython.display import clear_output


import os
import time
import random

board = [""] + [" "] * 9
def display_board(board):
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print('- - -')
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print('- - -')
    print(board[1]+ '|' + board[2]+ '|' + board[3])

def win_check(board,mark):
    return((board[7] == mark and board[8] == mark and board[9] == mark) or #top
    (board[4] == mark and board[5] == mark and board[6] == mark) or #mid
    (board[1] == mark and board[2] == mark and board[3] == mark) or #bot
    (board[1] == mark and board[4] == mark and board[7] == mark) or #left
    (board[2] == mark and board[5] == mark and board[8] == mark) or #mid
    (board[3] == mark and board[6] == mark and board[9] == mark) or #right
    (board[1] == mark and board[5] == mark and board[9] == mark) or #left cross
    (board[3] == mark and board[5] == mark and board[7] == mark))  #right cross

def board_full (board):
    if " " in board:
        return False
    else:
        return True


while True:
    display_board(board)
    move = int(input("X , place a value empty space "))

    #Player X Code
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Please select another space")
        move = int(input("X , place a value empty space "))
        board[move] = 'X'

    if win_check(board, 'X'):
        display_board(board)
        print("X is the winner")
        break

    Full = board_full (board)

    if Full == True:
        print("TIE GAME")
        display_board(board)
        break

    display_board(board)

    #Player O Code

    move = int(input("O, place a value in an empty space "))

    if board[move] == ' ':
        board[move] = 'O'
    else:
        print("Please select another space")
        move = int(input("O, place a value in an empty space "))
        board[move] = 'O'

    if win_check(board, 'O'):
        display_board(board)
        print("O is the winner")
        break

    Full = board_full (board)

    if Full == True:
        print ("TIE GAME")
        display_board(board)
        break
