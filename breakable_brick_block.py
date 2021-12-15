
class BreakableBrickBlock:

    def __init__(self, y:int):
        # The y coordinate takes the hight at which the blocks will be generated
        self.y = y
        # This is a list of the coordinates of the different blocks along the level
        self.bBBB = [320, 352, 384, 672, 688, 768, 784, 800, 928, 944]
    # A method that 'updates' the block for being hit from below
    # To be implemented in the 4th sprint
