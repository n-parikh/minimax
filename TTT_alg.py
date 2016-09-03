#!/usr/bin/python3

from tkinter import *

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

myMove = False

win = Tk()
frame = Frame(win)
frame.grid()
restart0 = Button(win, width=10, height=5, state=DISABLED, bg='black')
restart1 = Button(win, text="RESTART", width=10, height=5)
restart2 = Button(win, width=10, height=5, state=DISABLED, bg='black')


def onButtonClick(row, column):
    global myMove, board
    if(myMove == False):
        # setting the value in the board, 1 = player, -1 = AI
        board[row][column] = 1
        button_pressed = findButton(row, column)
        if(button_pressed != None):
            button_pressed["text"] = "X"
            myMove = True
    else:
        print(myMove)
        # AImove(board, myMove)


def findButton(row, column):
    for children in frame.children.values():
        info = children.grid_info()
        if(info["row"] == row and info["column"] == column):
            return children
    return None


sumList = [0, 0, 0, 0, 0, 0, 0, 0]


def checkWinDiag(board):
    i = 0
    AIsum_1 = 0
    Psum_1 = 0
    AIsum_2 = 0
    Psum_2 = 0
    winner = None
    for i in range(3):

        if(board[i][i] == -1):
            AIsum_1 += board[i][i]
        elif(board[i][i] == 1):
            Psum_1 += board[i][i]
    for j in range(3):
        if(board[2 - j][j] == -1):
            AIsum_2 += board[2 - j][j]
        elif(board[2 - j][j] == 1):
            Psum_2 += board[2 - j][j]

    if(AIsum_1 == -3):
        winner = -1
    elif(Psum_1 == 3):
        winner = 1
    elif(Psum_2 == 3):
        winner = 1
    elif(AIsum_2 == -3):
        winner = -1
    else:
        winner = None

    return winner


def checkRowsAndColumns(board):
    # 3, 7, 6, 2

    for m in range(3):

        sumList[3] = 0
        sumList[7] = 0
        sumList[6] = 0
        sumList[2] = 0

        for c in range(3):
            # columns
            if(board[c][m] == -1):
                sumList[2] += board[c][m]
            elif(board[c][m] == 1):
                sumList[6] += board[c][m]
        for r in range(3):
            # rows
            if(board[m][r] == -1):
                sumList[3] += board[m][r]
            elif(board[m][r] == 1):
                sumList[7] += board[m][r]
        # print(sumList[6])
        if(sumList[3] == -3):
            winner = -1
            return winner
            break
        elif(sumList[7] == 3):
            winner = 1
            return winner
            break
        elif(sumList[6] == 3):
            winner = 1
            return winner
            break
        elif(sumList[2] == -3):
            winner = -1
            return winner
            break

    winner = None
    return winner


def checkWinner():
    diag = checkWinDiag(board)
    r_c = checkRowsAndColumns(board)
    if(diag is None):
        return r_c
    else:
        return diag


def AImove(board):
    print(board)
    for x in range(3):
        for y in range(3):


for r in range(3):
    for c in range(3):
        i = 0
        Button(frame, height=5, width=10, command=(lambda row_=r, column_=c: onButtonClick(row_, column_))).grid(row=r, column=c)
        i += 1

# restart0.grid(row=3, column=0)
restart1.grid(row=3, column=0)
# restart2.grid(row=3, column=2)


win.mainloop()
