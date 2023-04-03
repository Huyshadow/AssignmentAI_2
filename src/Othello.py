import numpy as num
from constant import *

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


