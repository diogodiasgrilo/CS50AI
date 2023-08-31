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
    # Check if there are more X's or O's and return the player that has the next turn
    if not any(EMPTY in row for row in board):
        return O
    if sum(row.count(X) for row in board) > sum(row.count(O) for row in board):
        return O
    if sum(row.count(X) for row in board) == sum(row.count(O) for row in board):
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Return all the empty spaces on the board
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if the action is valid and return the board with the action made
    if action not in actions(board):
        raise Exception("Invalid action")
    deep_board = copy.deepcopy(board)
    deep_board[action[0]][action[1]] = player(board)
    return deep_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner or if there are no more empty spaces
    if winner(board) or not any(EMPTY in row for row in board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check who is the winner and return the number accordingly for the minimax
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def min_value_func(board):
    # Check if the game is over and return the number of who won
    if terminal(board):
        return utility(board)
    v = math.inf
    # Check all the possible actions and return the minimum value that is possible if the opponent plays optimally
    for action in actions(board):
        v = min(v, max_value_func(result(board, action)))
    return v


def max_value_func(board):
    # Check if the game is over and return the number of who won
    if terminal(board):
        return utility(board)
    v = -math.inf
    # Check all the possible actions and return the max value that is possible if the opponent plays optimally
    for action in actions(board):
        v = max(v, min_value_func(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 
    # Check if the game is already over
    if terminal(board):
        return None
    # Check if the player is X or O and return the optimal action for that player accordingly
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            min_value = min_value_func(result(board, action))
            if min_value > v:
                v = min_value
                optimal_action = action
    else:
        v = math.inf
        for action in actions(board):
            max_value = max_value_func(result(board, action))
            if max_value < v:
                v = max_value
                optimal_action = action
    return optimal_action

