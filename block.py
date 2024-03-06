import pygame
from color import *
from position import *

class Block(object):
    def __init__(self, id, cells):
        self.id = id
        self.colors = Colors.get_cell_colors()
        self.rotation = 0
        self.cells = cells
        self.cell_size = 40
        self.d_row = 0
        self.d_col = 0

    def move(self, d_row, d_col):
        self.d_row += d_row
        self.d_col += d_col
    
    def rotate(self):
        self.rotation += 1
        self.rotation = self.rotation % len(self.cells)
    
    def undo_rotate(self):
        self.rotation -= 1
        self.rotation = self.rotation % len(self.cells)
    
    def move_left(self):
        self.d_col -= 1
    
    def undo_move_left(self):
        self.d_col += 1

    def move_right(self):
        self.d_col += 1
    
    def undo_move_right(self):
        self.d_col -= 1
    
    def move_down(self):
        self.d_row += 1

    def undo_move_down(self):
        self.d_row -= 1
    
    def get_cell_positions(self):
        tiles = self.cells[self.rotation]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.d_row, position.col + self.d_col)
            moved_tiles.append(position)

        return moved_tiles

    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col*self.cell_size,
                tile.row*self.cell_size , self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, self.colors[self.id-1], tile_rect)


