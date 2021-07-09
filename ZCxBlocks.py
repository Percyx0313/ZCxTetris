# This is the module of ZCxBlock
# The block type:
#
# T         Z       I        L       
#    *      * *     * x * *  *   
#  * x *      x              x   
#             * *            * *  
#                           
#  RL      O        S        RS 
#  *       * *        * *    * *
#  x       x *      * x        x *
#  * * 
#================================================
#This class only has attribution Block
#The block retate clockwise 
class ZCxBlock:
    def __init__(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    def SetType_T(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    def SetType_Z(self):
        self.Block=[[0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,1,0],
                    [0,0,0,0,0]]
    def SetType_I(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    def SetType_L(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,1,0],
                    [0,0,0,0,0]]
    def SetType_RL(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,1,1,0,0],
                    [0,0,0,0,0]]
    def SetType_O(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,1,1,0],
                    [0,0,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    def SetType_S(self):
        self.Block=[[0,0,0,0,0],
                    [0,0,1,1,0],
                    [0,1,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    def SetType_RS(self):
        self.Block=[[0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,0,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]




    
    


