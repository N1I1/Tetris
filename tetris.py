import sys
import pygame
from game import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SCREEN_BAK_COLOR = (95, 93, 156) 
GRID_COLOR = (97, 150, 166)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

INITIAL_TIMER_INTERVAL = 600
TIMER_DECREASE_RATE = 1

timer_interval = INITIAL_TIMER_INTERVAL

GAME_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_UPDATE, timer_interval)

game = Game()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            timer_interval = max(timer_interval - TIMER_DECREASE_RATE, 300)
            pygame.time.set_timer(GAME_UPDATE, timer_interval)
            game.move_down()
    if game.game_over:
        running = False
    screen.fill(SCREEN_BAK_COLOR)
    game.grid.draw(surface=screen, color=GRID_COLOR)
    game.current_block.draw(screen=screen)
    pygame.display.update()
    clock.tick(60)