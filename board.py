import pyxel
# We import all the classes from the different files
from Mario import MARIO
from floor import Floor
from pipes import Pipes
from scoreboard import Scoreboard
from breakable_brick_block import BreakableBrickBlock
from question_block import QuestionBlock
from goomba import Goomba
from koopa_troopa import Koopa
from bushes import Bushes
from clouds import Clouds
# This imports the constants
import constant
# IMporting other libraries
from random import randint
# here starts the board class
class Board:
    def __init__(self, w, h):
        # This will give the height and width of the board
        self.width = w
        self.height = h
        
        # From here most of the classes are initialized, which are neccessary to make most of drawings
        # Player
        self.mario = MARIO(0, 224, True)
        # Floor
        self.floor = Floor(240)
        # Breakablebrick
        self.bb = BreakableBrickBlock(176)
        # Question block on height 3 blocks
        self.qb3 = QuestionBlock(176)
        # Question block on height 6 blocks
        self.qb6 = QuestionBlock(112)
        # Pipes
        self.pipes = Pipes(192)
        # Scoreboard
        self.scoreboard = Scoreboard(400, 0, 000000)
        
        # Decoration
        self.clouds = Clouds(randint(60, 70))
        self.bushes = Bushes(224)
        # Enemies
        # Koopa
        self.koopa = Koopa(216)
        # Goomba
        self.goomba = Goomba(224)
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # this is responsible for the control of Mario
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=True, period=1):
            self.mario.move('right', self.width)
        if pyxel.btnp(pyxel.KEY_LEFT, hold=True, period=1):
            self.mario.move('left', self.width)
        if pyxel.btnp(pyxel.KEY_UP, hold = True, period=1):
            self.mario.move('up', self.height)
        else:
            self.mario.move('down', self.height)
        # Here we add the up or 'jump button'
        # And the methods that will modify the movement of the enemies
        # koopa troopa enemie movement constant update
        # the koopa is simpler, it moves in a periodic way 
        self.koopa.koopa_move()
        # Goomba enemy movement 
        # The goomba is the hard one, it needs to check collisions with
        # All of the elements in the environment -> not do this part
        self.goomba.goomba_move()
        # Here the update method of the different blocks where to be added
        
    def draw(self):
        pyxel.cls(12)
        # The following two lines where meant to be used for debugging and testing the collision with platforms
        #pyxel.text(100,0, str(self.player.decrease), 6)
        #pyxel.text(100,10, str(self.player.moved_middle), 8)
        # Scoreborad drawing
        # Time tracking
        if pyxel.frame_count % 60 == 0:
            self.scoreboard.time -= 1 
        pyxel.text(200, 0, 'Time', 7)
        pyxel.text(200, 7, str(self.scoreboard.time),7)
        # Score
        pyxel.text(0, 0, 'Scoreboard', 7)
        pyxel.text(0, 10,str(self.scoreboard.score), 7)
        # Coins
        # Coin image
        pyxel.blt(100, 9, constant.COIN_IMAGE[0], constant.COIN_IMAGE[1], constant.COIN_IMAGE[2], constant.COIN_IMAGE[3],constant.COIN_IMAGE[4] )
        pyxel.text(110, 10, 'X'+str(self.scoreboard.coin_amount), 7)
        
        # The following draws the elements across the 4 screens 
        for i in range(0, 1025, 16): 
            # Decorations of the level
            # Clouds
            # Functionality: most of the conditionals will draw the corresponding sprite if it's found in the list predefined, such list has the x coordinates
            # Mostly are defined off-screen. If not the sprite is not drawn, pretty straightforward. The images are moved with respect to the 'decrease' variable
            # of Mario and thus makes the level have the illusion of moving through the level.
            if i in self.clouds.coordinates:
                pyxel.blt(i -self.mario.decrease, self.clouds.y, constant.CLOUD_IMAGE[0], constant.CLOUD_IMAGE[1], constant.CLOUD_IMAGE[2], constant.CLOUD_IMAGE[3], constant.CLOUD_IMAGE[4])
            # Bushes
            if i in self.bushes.bush_coor:
                pyxel.blt(i-self.mario.decrease, self.bushes.y, constant.BUSH_IMAGE[0], constant.BUSH_IMAGE[1], constant.BUSH_IMAGE[2], constant.BUSH_IMAGE[3], constant.BUSH_IMAGE[4])
            # Elements that interact with the player
            # Floor Blocks
            if i not in self.floor.not_blocks:
                pyxel.blt(i-self.mario.decrease,self.floor.y, constant.FLOOR_IMAGE[0], constant.FLOOR_IMAGE[1], constant.FLOOR_IMAGE[2], constant.FLOOR_IMAGE[3], constant.FLOOR_IMAGE[4])
            # Breakable bricks
            if i in self.bb.bBBB:
                pyxel.blt(i-self.mario.decrease, self.bb.y, constant.BRICK[0], constant.BRICK[1], constant.BRICK[2], constant.BRICK[3], constant.BRICK[4])
            # Question blocks at 'height' of 3 blocks
            if i in self.qb3.bQB3:
                pyxel.blt(i-self.mario.decrease, self.qb3.y, constant.QUESTION_BLOCK_IMAGE[0], constant.QUESTION_BLOCK_IMAGE[1], constant.QUESTION_BLOCK_IMAGE[2], constant.QUESTION_BLOCK_IMAGE[3], constant.QUESTION_BLOCK_IMAGE[4])
            # Question blocks at 'height' of 6 blocks
            if i in self.qb6.bQB6:
                pyxel.blt(i-self.mario.decrease, self.qb6.y, constant.QUESTION_BLOCK_IMAGE[0], constant.QUESTION_BLOCK_IMAGE[1], constant.QUESTION_BLOCK_IMAGE[2], constant.QUESTION_BLOCK_IMAGE[3], constant.QUESTION_BLOCK_IMAGE[4])
            # Conditional that draws pipes
            if i in self.pipes.pipes_list:
                # The 'single' hegiht pipe
                if i == self.pipes.pipes_list[0]:
                    pyxel.blt(i-self.mario.decrease, self.pipes.y+16, constant.PIPE_IMAGE[0], constant.PIPE_IMAGE[1], constant.PIPE_IMAGE[2], constant.PIPE_IMAGE[3], constant.PIPE_IMAGE[4])
                # The 'double' height pipe
                if i == self.pipes.pipes_list[1]:
                    # The for loop inside ensures the bottom pipe is drawn before the 'top pipe'
                    # So that it gives the 1 single pipe drawing
                    # The inner for loop ensures that the lower pipe is drawn before the top pipe, so to make the pipe look like a continuous one
                    for o in range(0,2):
                        pyxel.blt(i-self.mario.decrease, self.pipes.y+(16-(o*16)), constant.PIPE_IMAGE[0], constant.PIPE_IMAGE[1], constant.PIPE_IMAGE[2], constant.PIPE_IMAGE[3], constant.PIPE_IMAGE[4])
            # The enemy drawings
            # Since we couldn't think of a conditional that made enemies appear every x seconds we decided to go for 'predefined randomness'
            # That is we generate them throughout the level in an order 
            # This generates a goomba
            if i in self.goomba.goomba_position:
                pyxel.blt(i-self.mario.decrease + self.goomba.goomba_x ,  self.goomba.goomba_y, constant.GOOMBA_IMAGE[0] , constant.GOOMBA_IMAGE[1], constant.GOOMBA_IMAGE[2], constant.GOOMBA_IMAGE[3], constant.GOOMBA_IMAGE[4], 12)
            # This will generate a koopa
            if i in self.koopa.koopa_position:
                pyxel.blt(i - self.mario.decrease + self.koopa.koopa_x , self.koopa.koopa_y, constant.KOOPA_TROOPA_IMAGE[0] , constant.KOOPA_TROOPA_IMAGE[1], constant.KOOPA_TROOPA_IMAGE[2], constant.KOOPA_TROOPA_IMAGE[3], constant.KOOPA_TROOPA_IMAGE[4], 12)
        
        # Player drawing sprite and movement    
        pyxel.blt(self.mario.x, self.mario.y, 0, constant.MARIO_IMAGE[0], constant.MARIO_IMAGE[2], constant.MARIO_IMAGE[3], constant.MARIO_IMAGE[4], 12)
