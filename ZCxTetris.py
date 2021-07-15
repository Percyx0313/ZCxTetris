#================================================
import pygame
import random
from ZCxBlocks import ZCxBlock
#================================================


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
class ZCxTetris:
    Block_Type=["O","I","T","Z","S","J","L"]
    clear = 0
    score = 0
    state = "start"
    field = []
    HEIGHT = 0
    WIDTH = 0
    startX = 100
    startY = 50
    zoom = 20
    #============================================
    def __init__(self, height, width):
        self.width = 3+width+3
        self.height = 3+height+3
        self.block = ZCxBlock()
        self.field = []
        self.ptBlock_x=5
        self.ptBlock_y=0
        #create an empty field
        #creat by row major
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_line.append(0)
            self.field.append(new_line)
    #============================================
    def create_block(self,type):
        if type=="T":
            self.block.SetType_T()
        if type=="I":
            self.block.SetType_I()
        if type=="L":
            self.block.SetType_L()
        if type=="J":
            self.block.SetType_J()
        if type=="O":
            self.block.SetType_O()
        if type=="S":
            self.block.SetType_S()
        if type=="Z":
            self.block.SetType_Z()
    #============================================
    def intersect(self):
        for i in range(4):
            for j in range(4):
                if self.field[i + self.ptBlock_y][j + self.ptBlock_x]==1 and self.block.Block[i][j]==1:
                    return True
                    
        return False
    #============================================
    def freeze_block(self):
        for i in range(4):
            for j in range(4):
                    if self.block.Block[i][j]==1:
                        self.field[i + self.ptBlock_y][j + self.ptBlock_x] = self.block.Block[i][j]
        self.block.BlockType=None
        return self.clear_line()
    #============================================
    def clear_line(self):
        lines = 0
        row_sum=0
        cancle_row=[]
        for i in range(self.height-3-3):
            row_sum=0
            for j in range(self.width-3-3):
                if(self.field[3+i][j+3]>0):
                    row_sum+=1
            if(row_sum==self.width-3-3):
                cancle_row.append(i+3)
                for index in range(self.width-3-3):
                    self.field[i+3][index+3]=0
                    lines+=1
        if lines==0:
            return 0
        for row in cancle_row:
            for upper_row in range(row-1):
                for x in range(self.width-3-3):
                    self.field[row-upper_row][x+3]=self.field[row-upper_row-1][x+3]
        return lines+self.clear_line()
    #============================================
    # makes the black fall down until it gets into a collision
    def fall(self):
        while not (self.intersect() or self.unbound()):
            self.ptBlock_y += 1
        self.ptBlock_y -= 1
        return self.freeze_block()
        
    #============================================
    def go_down(self):
        self.ptBlock_y += 1
        if self.intersect() or self.unbound():
            self.ptBlock_y -= 1
            return self.freeze_block()
        return 0
         
    #============================================
    def go_side(self, dx):
        #dx = 1 for right, -1 for left
        previous_x = self.ptBlock_x
        self.ptBlock_x += dx
        #if there is collision during go_side, then revert back to previously saved position
        if self.intersect() or self.unbound() or self.ptBlock_x<0 or self.ptBlock_x>=self.width-3 or self.ptBlock_y<0 or self.ptBlock_y>=self.height-3:
            self.ptBlock_x = previous_x
    #============================================
    def rotation(self,LorR):
        test_case=0
        previous_stat = self.block
        shift=self.block.Rotate(LorR,test_case)
        self.ptBlock_x+=shift[0]
        self.ptBlock_y+=shift[1]
        if self.block.BlockType!="O":
            while  (self.intersect() or self.unbound()) :
                self.block = previous_stat
                self.ptBlock_x-=shift[0]
                self.ptBlock_y-=shift[1]
                test_case+=1
                if test_case==4:
                    return 
                shift=self.block.Rotate(LorR,test_case)
                self.ptBlock_x+=shift[0]
                self.ptBlock_y+=shift[1]
                
            else:
                self.block.Rotate_State=self.block.Rotate_State_dic[(self.block.Rotate_State_dic[self.block.Rotate_State]+1)%4]
        else:
            if self.intersect() or self.unbound():
                self.block=previous_stat
                self.ptBlock_x-=shift[0]
                self.ptBlock_y-=shift[1]
            else:
                self.block.Rotate_State=self.block.Rotate_State_dic[(self.block.Rotate_State_dic[self.block.Rotate_State]+1)%4]
    #============================================
    def unbound(self):
        for i in range(4):
            for j in range(4):
                if self.block.Block[i][j]==1 and (i+self.ptBlock_y>=self.height-3 or j+self.ptBlock_x<3 or  j+self.ptBlock_x>=self.width-3):
                    print("unbound")
                    return True
        return False
    #============================================
    def game_over(self):
        for i in range(3):
            for j in range(self.width-3-3):
                if(self.field[i][j+3])==1:
                    return True
        return False
        #============================================
        

#================================================================
# - main
def main():
    global level
    global lines_to_clear
    gameover = False
    count = 0
    fps = 30
    auto_down = False
    round_score=0
    pygame.init()
    win = pygame.display.set_mode((400, 500))
    pygame.display.set_caption("ZCxTetris")
    clock = pygame.time.Clock()
    game = ZCxTetris(play_height, play_width)
    #================================================
    while not gameover:
        round_score=0
        if count<30:
            count+=1
        else:
            count=0
            auto_down=True
        #========================================
        if game.block.BlockType==None:
            game.create_block(random.choice(game.Block_Type))
            if game.block.BlockType=="I":
                game.ptBlock_x=5
                game.ptBlock_y=0
            else :
                game.ptBlock_x=5
                game.ptBlock_y=1
    
            next_block=True
        #========================================
        #Key board set up
        for event in pygame.event.get():
            count=0
            if event.type == pygame.QUIT:
                gameover = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_UP:
                    game.rotation(1)
                if event.key == pygame.K_z:
                    game.rotation(-1)
                if event.key == pygame.K_DOWN:
                    round_score+=game.go_down()
                if event.key == pygame.K_SPACE:
                    round_score+=game.fall()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if auto_down==True:
            auto_down=False
            game.ptBlock_y+=1
            if game.intersect() or game.unbound():
                game.ptBlock_y-=1
                round_score+=game.freeze_block()
        round_score+=game.clear_line()
        game.score=round_score**2
        if game.game_over():
            game.state="gameover"
        
        #========================================
        #draw background and block
        win.blit(background, (0, 0))
        for i in range(game.height-3-3):
            for j in range(game.width-3-3):
                pygame.draw.rect(win, (128, 128, 128), [game.startX + game.zoom * j, game.startY + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i+3][j+3] > 0:
                    pygame.draw.rect(win, colors[game.field[i+3][j+3]], [game.startX + game.zoom * j, game.startY + game.zoom * i, game.zoom - 2, game.zoom - 1])

        if game.block.BlockType!=None:
           for i in range(4):
                for j in range(4):
                    if game.block.Block[i][j]>0 and game.ptBlock_y+i>=3:
                        pygame.draw.rect(win, colors[game.block.Block[i][j]], [game.startX + game.zoom * ( j + game.ptBlock_x-3) + 1, game.startY + game.zoom * (i + game.ptBlock_y-3) + 1, game.zoom- 2, game.zoom - 2])
        #========================================
        font1 = pygame.font.SysFont('comicsans', 28, True)
        font2 = pygame.font.SysFont('comicsans', 50, True)
        text_score = font1.render("Score: " + str(game.score), True, (255, 255, 255))
        text_level = font1.render("Level: " + str(level), True, (255, 255, 255))
        text_lines_to_clear = font1.render("Lines to clear: " + str(lines_to_clear), True, (255, 255, 255))
        text_game_over1 = font2.render("Game Over", True, (255, 250, 205))
        win.blit(text_score, [25, 20])
        win.blit(text_lines_to_clear, [175, 20])
        win.blit(text_level, [175, 5])
        #========================================
        if game.state == "gameover":
            win.blit(text_game_over1, [110, 220])
            pygame.diaplay.flip()
            break
        pygame.display.flip()
        clock.tick(fps)
    #============================================

if __name__ == "__main__":
    # call the main function
    main()
