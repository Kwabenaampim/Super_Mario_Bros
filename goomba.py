class Goomba:
    def __init__(self, y:int):
    # The goomba_x variable is used to make the basic movement of the goomba enemy
        self.goomba_x = 0
    # Goomba_y is the height at which it will be generated
        self.goomba_y = y
    # The coordinates of the 3 different goombas in the level
        self.goomba_position = [288, 416, 928]
    def goomba_move(self):
        # Basic behaviour of the koopa
        # When generated it will always move to one direction
        # At the lack of a collision checker it will always move to the left
        # Implementation of death, and changing direction on hit meant to be performed on sprint 4
        self.goomba_x -= 0.25
