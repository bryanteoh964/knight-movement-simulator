import pygame

# Initialize the pygame
pygame.init

# create the screen
SCREEN_X = 600
SCREEN_Y = 600
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

# VARIABLES
x = 50
y = 10
z = 65
xy_shift = x + y
DEFAULT_IMAGE_SIZE = (x, x)

# Functions
def find_next_pos(x_pos, y_pos):
    if(x_pos == 0 and y_pos == 0):
        return[z, z]
    # if x is at the last column
    if(x_pos == (z + 7 * (xy_shift))):
        # if y isn't at the last row
        if(y_pos != 506):
            return [z, y_pos + (xy_shift)]
    else:
        return [x_pos + (xy_shift), y_pos]

# Title & Icon
pygame.display.set_caption("Knight Movement Simulator")

# Knight Piece
knight_piece = pygame.transform.scale(pygame.image.load('knight.png'), DEFAULT_IMAGE_SIZE)
knight_x = z
knight_y = (z + (7 * x) + (7 * y))
MOVE_DIST = x + y

# Implementing Grid Element
def implement_grid_elements():
    rows, cols = (8, 8)
    arr = [[pygame.transform.scale(pygame.image.load('square.png'), DEFAULT_IMAGE_SIZE)] * cols] * rows
    curr_x = 0
    curr_y = 0
    for elem in arr:
        for i in range(8):
            temp = find_next_pos(curr_x, curr_y)
            curr_x = temp[0]
            curr_y = temp[1]
            screen.blit(elem[i], (curr_x, curr_y))

# more functions
def knight(x, y):
    screen.blit(knight_piece, (x, y))

# Game loop
running = True
while running: 
    # Screen background
    screen.fill((225, 102, 102))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keystroke controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if knight_x != z:
                    knight_x -= MOVE_DIST
            if event.key == pygame.K_RIGHT:
                if knight_x != SCREEN_X - z - x:
                    knight_x += MOVE_DIST
            if event.key == pygame.K_UP:
                if knight_y != z:
                    knight_y -= MOVE_DIST
            if event.key == pygame.K_DOWN:
                if knight_y != SCREEN_Y - z - x:
                    knight_y += MOVE_DIST
            if event.key == pygame.K_RETURN:
                if knight_x != SCREEN_X - z - x:
                    knight_x += MOVE_DIST
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                knight_x = knight_x
    
    implement_grid_elements()
    knight(knight_x, knight_y)
    pygame.display.update()