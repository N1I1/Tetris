from block import *
from position import *

class IBlock(Block):
    def __init__(self):
        super().__init__(id=1,
            cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],
            })
        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id=2, 
            cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            })
        self.move(0, 4)

class LLBlock(Block):
    def __init__(self):
        super().__init__(id=3, 
            cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
            })
        self.move(0, 3)

class RLBlock(Block):
    def __init__(self):
        super().__init__(id=4,
        cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],
        })
        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id=5,
        cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        })
        self.move(0, 3)

class LZBlock(Block):
    def __init__(self):
        super().__init__(id=6,
        cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],
        })
        self.move(0, 3)

class RZBlock(Block):
    def __init__(self):
        super().__init__(id=7,
        cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        })
        self.move(0, 3)
