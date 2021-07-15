# This is the module of ZCxBlock
# The block type:
#
# T        I         L       
#    *               *   
#  * x *    * x * *  x   
#                    * *  
#                           
#  J       O         S        Z 
#    *     * *         * *    * *
#    x     x *       * x        x *
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
    #--------------------------------------------
    Rotate_State_dic={"O":0,"R":1,"2":2,"L":3,0:"O",1:"R",2:"2",3:"L"}
    Wall_Kick_JLSTZ=(((0,0),(0,0),(0,0),(0,0)),((0,0),(1,0),(0,0),(-1,0)),((0,0),(1,-1),(0,0),(-1,-1)),((0,0),(0,2),(0,0),(0,2)),((0,0),(1,2),(0,0),(-1,2)))
    Wall_Kick_I=    (((0,0),(-1,0),(-1,1),(0,1)),((-1,0),(0,0),(1,1),(0,1)),((2,0),(0,0),(-2,1),(0,1)),((-1,0),(0,1),(1,0),(0,-1)),((2,0),(0,-2),(-2,0),(0,2)))
    Wall_Kick_O=((0,0),(0,-1),(-1,-1),(-1,0))
    #--------------------------------------------
    def __init__(self):
        self.Block=[[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.BlockType=None
        self.Rotate_Type=None
        self.Rotate_State="O"
        self.Wall_Kick_Type=None
    #--------------------------------------------
    def SetType_T(self):
        self.Block=[[0,1,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,0,0,0]]
        self.BlockType='T'
        self.Rotate_Type=3
        self.Rotate_State="O"
        self.Wall_Kick_Type="JLSTZ"
    #--------------------------------------------
    def SetType_I(self):
        self.Block=[[0,1,0,0],
                    [0,1,0,0],
                    [0,1,0,0],
                    [0,1,0,0]]
        self.BlockType='I'
        self.Rotate_Type=4
        self.Rotate_State="O"
        self.Wall_Kick_Type="I"
    #--------------------------------------------
    def SetType_L(self):
        self.Block=[[1,1,0,0],
                    [0,1,0,0],
                    [0,1,0,0],
                    [0,0,0,0]]
        self.BlockType='L'
        self.Rotate_Type=3
        self.Rotate_State="O"
        self.Wall_Kick_Type="JLSTZ"
    #--------------------------------------------
    def SetType_J(self):
        self.Block=[[0,1,0,0],
                    [0,1,0,0],
                    [1,1,0,0],
                    [0,0,0,0]]
        self.BlockType='J'
        self.Rotate_Type=3
        self.Rotate_State="O"
        self.Wall_Kick_Type="JLSTZ"
    #--------------------------------------------
    def SetType_O(self):
        self.Block=[[0,0,0,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,0,0,0]]
        self.BlockType='O'
        self.Rotate_Type=4
        self.Rotate_State="O"
        self.Wall_Kick_Type="O"
    #--------------------------------------------
    def SetType_S(self):
        self.Block=[[1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,0,0,0]]
        self.BlockType='S'
        self.Rotate_Type=3
        self.Rotate_State="O"
        self.Wall_Kick_Type="JLSTZ"
    #--------------------------------------------
    def SetType_Z(self):
        self.Block=[[0,0,1,0],
                    [0,1,1,0],
                    [0,1,0,0],
                    [0,0,0,0]]
        self.BlockType='Z'
        self.Rotate_Type=3
        self.Rotate_State="O"
        self.Wall_Kick_Type="JLSTZ"
    #--------------------------------------------
    # if L = -1 R =1
    def Change_Rotate_State(self,LorR):
        self.Rotate_State=ZCxBlock.Rotate_State_dic[ZCxBlock.Rotate_State_dic[(self.Rotate_State+LorR+4)%4]]
    #--------------------------------------------
    #The Rotate Function will return the shift vector that is from the Wall_Kick test case 
    # if L = -1 R =1
    def Rotate(self,LorR,WKtestnum=0):
        temp=[]
        if LorR==1:
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
        elif LorR==-1:
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
        shift_offset=[0,0]
        if self.Wall_Kick_Type=="JLSTZ":
            shift_offset[0]= LorR*(ZCxBlock.Wall_Kick_JLSTZ[WKtestnum][ZCxBlock.Rotate_State_dic[self.Rotate_State]][0]-ZCxBlock.Wall_Kick_JLSTZ[WKtestnum][(ZCxBlock.Rotate_State_dic[self.Rotate_State]+1)%4][0])
            shift_offset[1]= LorR*(ZCxBlock.Wall_Kick_JLSTZ[WKtestnum][ZCxBlock.Rotate_State_dic[self.Rotate_State]][1]-ZCxBlock.Wall_Kick_JLSTZ[WKtestnum][(ZCxBlock.Rotate_State_dic[self.Rotate_State]+1)%4][1])
        elif  self.Wall_Kick_Type=="I":
            shift_offset[0]=LorR*(ZCxBlock.Wall_Kick_I[WKtestnum][ZCxBlock.Rotate_State_dic[self.Rotate_State]][0]-ZCxBlock.Wall_Kick_I[WKtestnum][(ZCxBlock.Rotate_State_dic[self.Rotate_State]+1)%4][0])
            shift_offset[1]=LorR*(ZCxBlock.Wall_Kick_I[WKtestnum][ZCxBlock.Rotate_State_dic[self.Rotate_State]][1]-ZCxBlock.Wall_Kick_I[WKtestnum][(ZCxBlock.Rotate_State_dic[self.Rotate_State]+1)%4][1])
        elif self.Wall_Kick_Type=="O":
            shift_offset[0]=LorR*(ZCxBlock.Wall_Kick_O[ZCxBlock.Rotate_State_dic[self.Rotate_State]][0]-ZCxBlock.Wall_Kick_O[(ZCxBlock.Rotate_State_dic[self.Rotate_State]+1)%4][0])
            shift_offset[1]=LorR*(ZCxBlock.Wall_Kick_O[ZCxBlock.Rotate_State_dic[self.Rotate_State]][1]-ZCxBlock.Wall_Kick_O[(ZCxBlock.Rotate_State_dic[self.Rotate_State]+1)%4][1])

        return shift_offset
    #--------------------------------------------
    def show_block(self):
        for y in range(4):
            print(self.Block[y][0],self.Block[y][1],self.Block[y][2],self.Block[y][3])
    #--------------------------------------------