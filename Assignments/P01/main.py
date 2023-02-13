import pygame as py
import random
from Logic import *

py.init()

# initial set up
WIDTH = 400
HEIGHT = 500
screen = py.display.set_mode([WIDTH, HEIGHT])
py.display.set_caption('2048')
timer = py.time.Clock()
fps = 60
font = py.font.Font('sans.ttf', 24)

# 2048 game color library
# 2048 game color library
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

# game variables initialize
game = game_board()

game.add_piece()



# draw background for the board
def draw_board():
    py.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)


#
#   Description: Draw's the pieces on the board. We don't have to return anything
#                bcs numpy makes a shallow copy
#
#   Params:      board - the game board
#
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = color['other']
            # draws the rectangle for the number
            py.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            # if there's a number we display the number 
            if value > 0: 
                value_len = len(str(value))
                font = py.font.Font('sans.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)                 # render the text
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))      # get rect. for text
                screen.blit(value_text, text_rect)                                      # display 
                py.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5) # outline the squares

#
#   Displays the score of the game
#
def display_score(score):
    font = py.font.Font('sans.ttf', 26)
    value_text = font.render(f"score: {score}", True, 'black')
    text_rect = value_text.get_rect(topleft=(10, 440))
    screen.blit(value_text, text_rect)



# main game loop
game_over = False
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(game.board)
    display_score(game.score)

    if game_over:
        font = py.font.Font('sans.ttf', 32)
        value_text = font.render(f"GAME OVER", True, 'black')
        text_rect = value_text.get_rect(center=(200, 420))
        screen.blit(value_text, text_rect)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        
        # check if one of the arrow keys was pressed 
        if event.type == py.KEYDOWN and (event.key >= 1073741903 and event.key <= 1073741906):
                
            if event.key == py.K_UP:
                changed = game.move('up')
            elif event.key == py.K_RIGHT:
                changed = game.move('right')
            elif event.key == py.K_DOWN:
                changed = game.move('down')
            elif event.key == py.K_LEFT:
                changed = game.move('left')

            # if there was a changed in the game state then add a piece
            if changed == True:
                game.add_piece()

            # game does not have valid moves
            if not game.has_valid_move():
                game_over = True

    py.display.flip()

py.quit()
