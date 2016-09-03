

board = [[1, None, None],
         [None, None, None],
         [None, None, None]]

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
        winner = -1
    elif(sumList[4] == 3):
        winner = 1
    elif(sumList[5] == 3):
        winner = 1
    elif(sumList[1] == -3):
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


def checkWinner(board):
    diag = checkWinDiag(board)
    r_c = checkRowsAndColumns(board)
    if(diag is None):
        return r_c
    else:
        return diag

myMove = True
numNodes = 0


def AImove(board, player):

    return AIrecursive(board, player)
    myMove = False

# for player, false is AI and true is player
# AI is minimizing here.


def AIrecursive(board, player):
    global numNodes
    numNodes += 1
    nextboardlist = list()
    winner = checkWinner()
    if(winner is not None):
        return winner
    else:
        if(player is False):
            x = -1
        else:
            x = 1
        for i in range(3):
            for j in range(3):
                if(board[i][j] is None):
                    board[i][j] = x
                    AIrecursive(board, not(player))
                    board[i][j] = None

best_move = None
scoreList = [0]
movesList = [0]


def minimax(board, player):
    global best_move, scoreList, movesList
    winner = checkWinner(board)
    print(winner)
    if(winner is None):
        if(player is False):
            x = -1
        else:
            x = 1
        for i in range(3):
            for j in range(3):
                if(board[i][j] is None):
                    board[i][j] = x
                    scoreList.append(minimax(board, not(player)))
                    movesList.append(board)
                    board[i][j] = None
                else:
                    continue
        if(player is False):
            # min calc
            min_index = scoreList.index(min(scoreList))
            best_move = movesList[min_index]
            # print(scoreList[min_index])
            return scoreList[min_index]
        else:
            # max calc
            max_index = scoreList.index(max(scoreList))
            best_move = movesList[max_index]
            # print(scoreList[max_index])
            return scoreList[max_index]
    else:
        # end state, value is -1 or 1
        return winner

score = minimax(board, False)
print(best_move, score)
