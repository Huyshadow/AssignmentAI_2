import copy
import numpy as num 
import time
from constant import *

#X = 1
#O = -1

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
        self.board[self.n // 2, self.n // 2] = O_SIGNAL
        self.board[self.n // 2 - 1, self.n // 2 - 1]= O_SIGNAL
        self.board[self.n // 2 - 1, self.n // 2] = X_SIGNAL
        self.board[self.n // 2, self.n // 2 - 1] = X_SIGNAL
        self.X_score = 2 
        self.O_score = 2
        self.no_moves_sema = 0
        self.last_move = None

    def move_possible(self, player_to_move): # Chỉ có thể là 1 hoặc -1
        possible_move = []
        self.board[self.board == VALID_MOVE] = EMPTY
        pieces = num.argwhere(self.board == player_to_move)
        opponent = O_SIGNAL if player_to_move == X_SIGNAL else X_SIGNAL
        for moves in pieces:
            for direction in DIRECTIONS:
                self.move_part(player_to_move, opponent, moves, direction, possible_move)
        if len(possible_move) == 0 :
            self.no_moves_sema += 1 
        else:
            self.no_moves_sema = 0
        return possible_move
    
    def invalid_move(self, x, y):
        return x < 0 or y < 0 or x >= self.n or y >= self.n

    def move_part(self, player, opponent, start, dir, moves):
        move_x = 0 
        move_y = 0 
        if dir in ("n", "n_w", "n_e"):
            move_x = move_x - 1
        elif dir in ("s", "s_w", "s_e"):
            move_x = move_x + 1
        if dir in ("w", "n_w", "s_w"):
            move_y = move_y - 1
        elif dir in ("e", "n_e", "s_e"):
            move_y = move_y + 1
        x = start[0] + move_x
        y = start[1] + move_y

        last_seen_oppo = None
        while not self.invalid_move(x,y):
            if self.board[x,y] == opponent:
                last_seen_oppo = [x,y]
            elif self.board[x,y] == player: break
            elif self.state[x,y] == EMPTY:
                if last_seen_oppo:
                    if not self.invalid_move(x,y):
                        self.board[x,y] = VALID_MOVE
                        moves.append((Move(x,y)))
                        break
                break
            elif self.state[x,y] == VALID_MOVE:
                break
            x += move_x
            y += move_y


    def move_choosing(self, player_to_move, move):
        self.board[self.board == VALID_MOVE] = EMPTY
        self.board[move[0], move[1]] = player
        self.last_play = Move(move[0], move[1])
        if player_to_move == X_SIGNAL:
            self.X_score += 1
        else:
            self.O_score += 1
        opponent = O_SIGNAL if player_to_move == X_SIGNAL else X_SIGNAL
        for direction in DIRECTIONS:
            self.movechosing_single_dir(player_to_move, opponent, move, direction)

    def movechosing_single_dir(self, player, opponent, move, dir):
        move_x = 0
        move_y = 0
        if dir in ("n", "n_w", "n_e"):
            move_x = move_x - 1
        elif dir in ("s", "s_w", "s_e"):
            move_x = move_x + 1
        if dir in ("w", "n_w", "s_w"):
            move_y = move_y - 1
        elif dir in ("e", "n_e", "s_e"):
            move_y = move_y - 1
        
        x = move[0] + move_x
        y = move[1] + move_y

        catch_opponent= []
        while not self.invalid_move(x,y):
            if self.board[x,y] == opponent:
                catch_opponent.append([x,y])
            elif self.board[x,y] == player:
                if player == X_SIGNAL:
                    self.X_score += len(catch_opponent)
                    self.O_score -= len(catch_opponent)

        
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
        """ self.total_branching_factor = 0
        self.total_effective_branching_factor = 0
        self.total_execution_time = 0 """


    def alpha_beta_pruning(cur_state, depth, player, opponent, alpha= float(-'inf'), beta= float('inf')):
        pass


#design curstate by using Othello.py
def select_move(cur_state, player_to_move, remain_time): 

    #Currenr state là một list 2 chiều có độ dại mỗi chiều là 8
    opponent = O_SIGNAL if player_to_move == X_SIGNAL else X_SIGNAL
    #Calculate time
    start_time = time.time()

    time_using = time.time() - start_time
    if(time_using > 3):
        print("Optimize algorithm hurry")
    remain_time -= time_using
    if(remain_time < 0):
        print("Lose")
    



    
    
