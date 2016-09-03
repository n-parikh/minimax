

board = [[1, None, None],
         [None, None, None],
         [1, None, -1]]

sumList = [0, 0, 0, 0, 0, 0, 0, 0]


def checkWinDiag(board):

    # AIsum_1  0
    # AIsum_2  1
    # Psum_1  4
    # Psum_2  5
    # AIsum_r 3
    # Psum_r 7
    # AIsum_c 2
    # Psum_c 6

    winner = None
    for i in range(3):
        if(board[i][i] == -1):
            sumList[0] += board[i][i]
        elif(board[i][i] == 1):
            sumList[4] += board[i][i]
    for j in range(3):
        if(board[2 - j][j] == -1):
            sumList[1] += board[2 - j][j]
        elif(board[2 - j][j] == 1):
            sumList[5] += board[2 - j][j]
    if(sumList[0] == -3):
        winner = -10
    elif(sumList[4] == 3):
        winner = 10
    elif(sumList[5] == 3):
        winner = 10
    elif(sumList[1] == -3):
        winner = -10
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
            winner = -10
            return winner
            break
        elif(sumList[7] == 3):
            winner = 10
            return winner
            break
        elif(sumList[6] == 3):
            winner = 10
            return winner
            break
        elif(sumList[2] == -3):
            winner = -10
            return winner
            break

    winner = None
    return winner


def checkWinner(board):
    diag = checkWinDiag(board)
    r_c = checkRowsAndColumns(board)
    if(diag is None and r_c is None):
        return 0
    elif(diag is None and r_c is not None):
        return r_c
    else:
        return diag

myMove = True
numNodes = 0


# for player, false is AI and true is player
# AI is minimizing here.


best_move = None
scoreList = []
movesList = []


def getPossibleMoves(board):
    possibleMoves = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] is None):
                possibleMoves.append((i, j))
    return possibleMoves


def getNewBoard(board, move, player):
    if(player is False):
        x = -1
    else:
        x = 1
    board[move[0]][move[1]] = x
    return board


def checkMinMax(board, player):
    global best_move, scoreList, movesList, possibleMoves

    if(player is False):
        # min calc
        min_index = scoreList.index(min(x for x in scoreList if x is not None))
        # print(min_index)
        best_move = movesList[min_index]
        # print(scoreList[min_index])
        return scoreList[min_index]
    else:
        # max calc
        max_index = scoreList.index(max(x for x in scoreList if x is not None))
        # print(max_index)
        best_move = movesList[max_index]
        # print(scoreList[max_index])
        return scoreList[max_index]


def minimax(board, player):
    global best_move, scoreList, movesList, numNodes, possibleMoves
    numNodes += 1
    gen = []
    for k in board:
        for y in k:
            gen.append(y)

    if(None in gen):
        game_over = False
    else:
        return checkWinner(board)

    if(game_over is False):

        pMove = getPossibleMoves(board)
        for a in pMove:
            nextState = getNewBoard(board, a, player)
            scoreList.append(minimax(nextState, not(player)))
            movesList.append(a)

        return checkMinMax(board, player)


score = minimax(board, False)
print(best_move, score)

end = minimax(board, False)
if(end == 10):
    messagebox.showinfo("Game Over", "Player Won")
elif(end == -10):
    messagebox.showinfo("Game Over", "AI Won")
elif(end == 20):
    messagebox.showinfo("Game Over", "Tie")
