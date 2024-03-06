import random
import pygame
from blocks import *
from grid import *


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

class Game(object):
    def __init__(self):
        self.grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.remain_blocks = []
        self.fill_blocks()
        self.next_block = self.generate_block()
        self.current_block = self.generate_block()
        self.game_over = False

    def fill_blocks(self):
        self.remain_blocks = [IBlock(), OBlock(), TBlock(),
            LLBlock(), RLBlock(), LZBlock(), RZBlock()]
    
    def generate_block(self):
        if len(self.remain_blocks) == 0:
            self.fill_blocks()
        block = random.choice(self.remain_blocks)
        self.remain_blocks.remove(block)
        return block

    def move_down(self):
        self.current_block.move_down()
        if not self.is_block_inside() or self.is_collision():
            self.current_block.undo_move_down()
            self.lock_block()

    def move_left(self):
        self.current_block.move_left()
        if not self.is_block_inside() or self.is_collision():
            self.current_block.undo_move_left()
    
    def move_right(self):
        self.current_block.move_right()
        if not self.is_block_inside() or self.is_collision():
            self.current_block.undo_move_right()
    
    def rotate(self):
        self.current_block.rotate()
        if not self.is_block_inside() or self.is_collision():
            self.current_block.undo_rotate()
    
    def is_block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(row=tile.row, col=tile.col):
                return False
        return True
    
    def is_collision(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.cells[tile.row][tile.col] != 0:
                return True
        return False
    
    def lock_block(self):
        self.grid.add_block(self.current_block)
        self.current_block = self.next_block
        self.next_block = self.generate_block()
        self.clear_rows() 
        self.game_over = self.is_game_over()
    
    def clear_rows(self):
        self.grid.clear_rows()

    def is_game_over(self):
        for i in range(COLS):
            if self.grid.cells[0][i] != 0:
                return True
        return False