import pyxel
class Koopa:
    def __init__(self, x: int, y: int):
        # Parameter x is the postion where the koopa will appear
        # Parameter y is the other component of the position
        self.koopa_x = x
        self.koopa_y = y
        self.moved_right = 0
        self.moved_left = 48
    def koopa_move(self):
        # This block creates the back and forth movement of the enemy
            if pyxel.frame_count % 60 and self.moved_right < 48:
                self.koopa_x -= 2
                self.moved_right += 2
                if self.moved_right == 48:
                    self.moved_left = 48
            elif pyxel.frame_count % 60 and self.moved_left > 0:
                self.koopa_x += 2
                self.moved_left -= 2
                if self.moved_left == 0:
                    self.moved_right = 0
