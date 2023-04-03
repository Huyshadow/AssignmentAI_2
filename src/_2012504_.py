import copy
import numpy as num 
from constant import *
#BLACK = -1
#WHITE = 1

class Move:
    def __init__(self, x= -1, y = -1, value = None):
        self.x = x 
        self.y = y 
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


class Problem:
    def __init__(self,n):
        self.n = n 
        self.board = num.zeros((self.n,self.n), dtype = num.int)
        self.board[self.n // 2, self.n // 2] = WHITE
        self.board[self.n // 2 - 1, self.n // 2 - 1]= WHITE
        self.board[self.n // 2 - 1, self.n // 2] = BLACK
        self.board[self.n // 2, self.n // 2 - 1] = BLACK
        # self.X_score = 2 
        # self.Y_score = 2
        # self.no_moves_sema = 0
        # self.last_move = None
    def move_possible(self, player_to_move): # Chỉ có thể là 1 hoặc -1
        possible_move = []
        self.board[self.board == VALID_MOVE] = EMPTY
        pieces = num.argwhere
        opponent = WHITE if player_to_move == BLACK else BLACK

class AI_Using:
    def __init__(self, identifier, agent_type, hints, depth, evaluation_fn, move_ordering):
        self.identifier = identifier
        self.agent_type = agent_type
        self.hints = hints
        self.depth = depth
        self.evaluation_fn = evaluation_fn
        self.move_ordering = move_ordering
        self.turns = 0
        self.branches_evaluated = 0
        self.nodes_per_level = [0]*(self.depth + 1)
        self.total_branching_factor = 0
        self.total_effective_branching_factor = 0
        self.total_execution_time = 0

#Release more in tomorrow

def alpha_beta_pruning(cur_state, depth, player, opponent, alpha= float(-'inf'), beta= float('inf')):
    pass


#design curstate by using Othello.py
def select_move(cur_state, player_to_move, remain_time): 
    opponent = WHITE if player_to_move == BLACK else BLACK
    
    
