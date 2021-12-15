# here we imported the neccessary libraries for the code to work
import pyxel
import constant
from board import Board
# We initialize the board class with its height and width
board = Board(256, 256)
# This is the standard method of initializing the app
pyxel.init(board.width,board.height, caption = constant.CAPTION, fps = 60)
# This loads the assets file
pyxel.load('assets/marioassets.pyxres')
# This runs the 'app'
pyxel.run(board.update, board.draw)
