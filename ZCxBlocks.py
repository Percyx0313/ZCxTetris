# This is the module of ZCxBlock
# The block type:
#
# T        I        L       
#    *     * x * *  *   
#  * x *            x   
#                   * *  
#                           
#  J       O        S        Z 
#  *       * *        * *    * *
#  x       x *      * x        x *
#  * * 
#================================================
#           rotate type : O->R->2->L
#               J,L,S,T,Z Wall_Kick 
#       test1   test2   test3   test4   test5
#   O   (0,0)   (0,0)   (0,0)   (0,0)   (0,0)
#   R   (0,0)   (+1,0)  (+1,-1) (0,+2)  (+1,+2)
#   2   (0,0)   (0,0)   (0,0)   (0,0)   (0,0)
#   L   (0,0)   (-1,0)  (-1,-1) (0,+2)  (-1,+2)
#================================================
#                   I Wall_Kick
#       test1   test2   test3   test4   test5
#   O   (0,0)   (-1,0)  (+2,0)  (-1,0)  (+2,0)
#   R   (-1,0)  (0,0)   (0,0)   (0,+1)  (0,-2)
#   2   (-1,+1) (+1,+1) (-2,+1) (+1,0)  (-2,0)
#   L   (0,+1)  (0,+1)  (0,+1)  (0,-1)  (0,+2)
#================================================
#                   O Wall_Kick
#       test1   test2   test3   test4   test5
#   O   (0,0)
#   R   (0,-1)
#   2   (-1,-1)
#   L   (-1,0)
#================================================
#This class only has attribution Blocks
class ZCxBlock:
    def __init__(self):
        self.Block=[[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.BlockType=None
        self.Rotate_Type=None
    def SetType_T(self):
        self.Block=[[0,1,0,0],
                    [1,1,1,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.BlockType='T'
        self.Rotate_Type=3
    def SetType_I(self):
        self.Block=[[0,0,0,0],
                    [1,1,1,1],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.BlockType='I'
        self.Rotate_Type=4
    def SetType_L(self):
        self.Block=[[0,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,0,0]]
        self.BlockType='L'
        self.Rotate_Type=3
    def SetType_J(self):
        self.Block=[[0,1,0,0],
                    [0,1,0,0],
                    [1,1,0,0],
                    [0,0,0,0]]
        self.BlockType='J'
        self.Rotate_Type=3
    def SetType_O(self):
        self.Block=[[0,0,0,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,0,0,0]]
        self.BlockType='O'
        self.Rotate_Type=4
    def SetType_S(self):
        self.Block=[[0,1,1,0],
                    [1,1,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.BlockType='S'
        self.Rotate_Type=3
    def SetType_Z(self):
        self.Block=[[1,1,0,0],
                    [0,1,1,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.BlockType='Z'
        self.Rotate_Type=3
    def Rotate(self,LorR):
        temp=[]
        if LorR=="R":
            for i in range(len(self.Block)):
                temp.append(self.Block[i].copy())
            if self.Rotate_Type==3:
                for y in range(3):
                    for x in range(3):
                        index=6-3*x+y
                        self.Block[y][x]=temp[index//3][index%3]
        
            elif self.Rotate_Type==4:
                for y in range(4):
                    for x in range(4):
                        index=12-4*x+y
                        self.Block[y][x]=temp[index//4][index%4]
        elif LorR=="L":
            for i in range(len(self.Block)):
                temp.append(self.Block[i].copy())
            if self.Rotate_Type==3:
                for y in range(3):
                    for x in range(3):
                        index=3*x+2 -y
                        self.Block[y][x]=temp[index//3][index%3]
        
            elif self.Rotate_Type==4:
                for y in range(4):
                    for x in range(4):
                        index=4*x+3-y
                        self.Block[y][x]=temp[index//4][index%4]

    def show_block(self):
        for y in range(4):
            print(self.Block[y][0],self.Block[y][1],self.Block[y][2],self.Block[y][3])
       




    
    


