import pyxel
class Koopa:
    def __init__(self, y: int):
        # Parameter x is the postion where the koopa will appear
        # Parameter y is the other component of the position
        self.koopa_x = 0
        self.koopa_y = y
        # The following 2 parameters are used for the back and forth movement of the koopa
        self.moved_right = 0
        self.moved_left = 48
        # This is the coordinate of the koopa, at which it will be generated
        self.koopa_position =[672]
    def koopa_move(self):
        # This block creates the back and forth movement of the enemy
            if pyxel.frame_count % 60 and self.moved_right < 48:
            # The naming might be confusing but the code works the same
            # After moving 48 pixels(3 blocks)to the right, koopa will stop and
            # turn to the left to which will travel the same distance. Once
            # travelled that same distance it will go back to moving right
            # And in that way perpetually
                self.koopa_x -= 0.5
                self.moved_right += 0.5
                if self.moved_right == 48:
                    self.moved_left = 48
            elif pyxel.frame_count % 60 and self.moved_left > 0:
                self.koopa_x += 0.5
                self.moved_left -= 0.5
                if self.moved_left == 0:
                    self.moved_right = 0
