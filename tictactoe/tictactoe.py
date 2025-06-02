"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    if terminal(board):
        return EMPTY
    # counting moves made by each player
    for rows in board:
        for element in rows:
            if element == X:
                count_x += 1
            elif element == O:
                count_o += 1
    # turn of x if x and o have equal moves
    if count_x == count_o:
        return X
    # turn of o if x have more moves
    elif count_x > count_o:
        return O
    # default turn
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spaces = set()
    # checking for empty spots and adding to the set
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                empty_spaces.add((i, j))
    
    return empty_spaces


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # checking if the action made is outof bound
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise IndexError("Action coordinates out of bounds")
    
    # creating a deep copy and returning the deepcopy after making the move
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise ValueError
    new_board[action[0]][action[1]] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking for winner in column
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    
    # checking for winner in row
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        
    # checking for winner in diagonal
    if board[1][1] == board[2][2] and board[2][2] == board[0][0] and board[1][1] is not EMPTY:
        return board[1][1]
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] is not EMPTY:
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    new_actions = actions(board)
    # if turn of player x they should take the action which has maxvalue among moves with min value
    if player(board) == X:
        use = None
        v = -math.inf
        for action in new_actions:
            x = minvalue(result(board, action))
            if v < x:
                v = x
                use = action
        return use
    
    elif player(board) == O:
        use = None
        v = math.inf
        for action in new_actions:
            x = maxvalue(result(board, action))
            if v > x:
                v = x
                use = action
        return use
    
    else:
        return None


def minvalue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v


def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v