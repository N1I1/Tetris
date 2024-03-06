import pygame
from block import *
from color import *

ROWS = 20
COLS = 10
class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = self.width // COLS
        self.row = ROWS
        self.col = COLS
        self.rects = [[pygame.Rect(j*self.cell_size, i*self.cell_size, self.cell_size - 1, self.cell_size - 1)
                         for j in range(self.col)]for i in range(self.row)] 
        self.cells = [[0 for j in range(self.col)]for i in range(self.row)]

    def add_block(self, block):
        tiles = block.get_cell_positions()
        for tile in tiles:
            self.cells[tile.row][tile.col] = block.id
    
    def draw(self, surface, color):
        for i in range(self.row):
            for j in range(self.col):
                if self.cells[i][j] == 0:
                    pygame.draw.rect(surface, color, self.rects[i][j])
                else:
                    pygame.draw.rect(surface, Colors.get_cell_colors()[self.cells[i][j]-1], self.rects[i][j])

    def is_inside(self, row, col):
        if row >= 0 and row < self.row and col >= 0 and col < self.col:
            return True
        return False
    

    def is_full(self, row):
        for i in range(self.col):
            if self.cells[row][i] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for i in range(row, 0, -1):
            for j in range(self.col):
                self.cells[i][j] = self.cells[i-1][j]
        for j in range(self.col):
            self.cells[0][j] = 0
        

    def clear_rows(self):
        for i in range(self.row):
            if self.is_full(i):
                self.clear_row(i)