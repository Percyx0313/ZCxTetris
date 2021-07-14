import pygame
import random


#grid 10*20
#shapes: S, Z, I, O, J, L, T
#Load pic, music
background = pygame.image.load("./res/Image/bg.png")

#setting up global variables
win_width = 800
win_height = 700
rect_width = 300
rect_height = 600
play_width = 10
play_height = 20
level = 1
lines_to_clear = 1
colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
          (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
#================================================================


class Tetris:
    clear = 0
    score = 0
    state = "start"
    field = []
    HEIGHT = 0
    WIDTH = 0
    startX = 100
    startY = 50
    zoom = 20
    block = None

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.block = None
        self.field = []
        #create an empty field
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def create_block(self):
        self.block = ZCxBlock(3, 0)

    def intersect(self):
        intersect = False
        for i in range(4):
            for j in range(4):
                # making sure tiles containing figure are not 0
                if (i * 4) + j in self.block.get_block():
                    if(i+self.block.y) > (self.height - 1) or (j + self.block.x) > (self.width - 1) or (j + self.block.x) < 0 or self.field[i + self.block.y][j + self.block.x] > 0:
                        intersect = True
        return intersect

    def freeze_block(self):
        for i in range(4):
            for j in range(4):
                # identifies tiles containing figure vs empty tiles in the 4x4 matrix
                if i * 4 + j in self.block.get_block():
                    # give non zero values to all tiles containing the figure
                    self.field[i + self.block.y][j + self.block.x] = self.block.color
         # after freezing, check if any row is full and  remove that row
        self.clear_line()
        #create new block
        self.create_block()
        if self.intersect():
            self.state = "gameover"

    def clear_line(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(0, self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        # since height index in self.field is in descending order this code assigns the higher row to the lower row
                        self.field[i1][j] = self.field[i1 - 1][j]
    # add to score, if multiple lines are cleared at the same time exponentialize the score
        self.score += lines ** 2
        self.clear += lines
        self.check_level_up()

    def check_level_up(self):
        global level
        global lines_to_clear
        if self.clear >= level:
            level += 1
            lines_to_clear = level
            self.clear = 0
            return True
        else:
            lines_to_clear = level - self.clear
            return False

    # makes the black fall down until it gets into a collision
    def fall(self):
        while not self.intersect():
            self.block.y += 1
        if self.intersect():
            self.block.y -= 1
            self.freeze_block()

    def go_down(self):
        self.block.y += 1
        if self.intersect():
            self.block.y -= 1
            self.freeze_block()

    def go_side(self, dx):
        #dx = 1 for right, -1 for left
        previous_x = self.block.x
        self.block.x += dx
        #if there is collision during go_side, then revert back to previously saved position
        if self.intersect():
            self.block.x = previous_x

    def rotation(self):
        previous_rotation = self.block.rotation
        self.block.rotation()
        #if there is collision during rotation, then revert back to previouslu saved rotation
        if self.intersect():
            self.block.rotation = previous_rotation
#==============================================================


class ZCxBlock:
    # |0 |1 |2 |3 |
    # |4 |5 |6 |7 |
    # |8 |9 |10|11|
    # |12|13|14|15|
    blocks = [
        [[4, 5, 6, 7], [1, 5, 9, 13]],  # I
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9],
            [1, 5, 6, 9]],  # T
        # J
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 8, 9], [4, 5, 6, 10]],
        # L
        [[1, 2, 6, 10], [3, 5, 6, 7], [2, 6, 10, 11], [5, 6, 7, 9]],
        [[5, 6, 9, 10]],  # O
        # S
        [[1, 2, 4, 5], [0, 4, 5, 9], [5, 6, 8, 9], [1, 5, 6, 10]],
        # Z
        [[1, 2, 6, 7], [3, 6, 7, 10], [5, 6, 10, 11], [2, 5, 6, 9]]
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.blocks)-1)
        self.color = random.randint(1, (len(colors) - 1))
        self.rotation = 0
    #get the specific shape and color of the falling block

    def get_block(self):
        return self.blocks[self.type][self.rotation]

    def rotation(self):
        self.rotation = (self.rotation+1) % (len(self.blocks[self.type]))
# - main


def main():
    global level
    global lines_to_clear
    gameover = False
    count = 0
    fps = 30
    press_down = False
    pygame.init()
    win = pygame.display.set_mode((400, 500))
    pygame.display.set_caption("ZCxTetris")
    clock = pygame.time.Clock()
    game = Tetris(play_height, play_width)
    while not gameover:
        if game.block is None:
            game.create_block()
        count += 1
        if count > 100000:
            count = 0
        #make sure blocks fall down at same speed
        if count % (fps // level // 2) == 0 or press_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_UP:
                    game.rotation()
                if event.key == pygame.K_DOWN:
                    press_down = True
                if event.key == pygame.K_SPACE:
                    game.fall()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                press_down = False
        #win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        #draw grid
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(win, (128, 128, 128), [game.startX + game.zoom * j, game.startY + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(win, colors[game.field[i][j]], [game.startX + game.zoom * j, game.startY + game.zoom * i, game.zoom - 2, game.zoom - 1])

        if game.block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.block.get_block():
                        pygame.draw.rect(win, colors[game.block.color], [game.startX + game.zoom * ( j + game.block.x) + 1, game.startY + game.zoom * (i + game.block.y) + 1, game.zoom - 2, game.zoom - 2])
        font1 = pygame.font.SysFont('comicsans', 28, True)
        font2 = pygame.font.SysFont('comicsans', 50, True)
        text_score = font1.render("Score: " + str(game.score), True, (255, 255, 255))
        text_level = font1.render("Level: " + str(level), True, (255, 255, 255))
        text_lines_to_clear = font1.render("Lines to clear: " + str(lines_to_clear), True, (255, 255, 255))
        text_game_over1 = font2.render("Game Over", True, (255, 250, 205))
        #text_game_over2 = font1.render("Press ESC", True, (255, 250, 205))

        win.blit(text_score, [25, 20])
        win.blit(text_lines_to_clear, [175, 20])
        win.blit(text_level, [175, 5])
        if game.check_level_up():
            main()
        if game.state == "gameover":
            win.blit(text_game_over1, [110, 220])
            #win.blit(text_game_over2, [150, 275])
        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    # call the main function
    main()
