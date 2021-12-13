import pyxel
from board import Board
board = Board(256, 256)
pyxel.init(board.width,board.height, caption = 'Drawing test', fps = 60)
pyxel.load('assets/marioassets.pyxres')
pyxel.run(board.update, board.draw)
