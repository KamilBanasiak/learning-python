from abc import ABC, abstractmethod
from random import choice

class Player(ABC):
    
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
        
    def make_move(self):
        move = choice(self.moves)
        x1, y1 = self.position
        x2, y2 = move
        self.position = (x1 + x2, y1 + y2)
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
    def level_up(self):
        for i in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            self.moves.append(i)