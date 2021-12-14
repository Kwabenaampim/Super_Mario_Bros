import pyxel
import constant
from board import Board
board = Board(256, 256)
pyxel.init(board.width,board.height, caption = constant.CAPTION, fps = 60)
pyxel.load('assets/marioassets.pyxres')
pyxel.run(board.update, board.draw)
