import pygame
from pygame import image

pygame.init()

#grid 10*20
#shapes: S, Z, I, O, J, L, T
#Load pic, music
background = pygame.image.load("./res/Image/bg.png")
#setting up global variables
win = pygame.display.set_mode((800, 700))
pygame.display.set_caption("ZCxTetris")
win_width = 800
win_height = 700
rect_width = 300
rect_height = 600
top_left_x = (win_width - rect_width) // 2
top_left_y = win_height - rect_height
#shapes = [S, Z, I, O, J, L, T]



# functions
# - draw window
def draw_window(window):
    #window.fill((245, 245, 245))
    window.blit(background, (0, 0))
    pygame.draw.rect(window, (0, 0, 0), (top_left_x, top_left_y, rect_width, rect_height), 0)
    for i in range(20):
        pygame.draw.line(window, (128, 128, 128), (top_left_x, top_left_y+i*30), (top_left_x+rect_width, top_left_y+i*30))
        for j in range(10):
            pygame.draw.line(window, (128, 128, 128), (top_left_x+j*30, top_left_y), (top_left_x+j*30, top_left_y+rect_height))
    pygame.display.update()

# - main
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_window(win)
pygame.quit()
