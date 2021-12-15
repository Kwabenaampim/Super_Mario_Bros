class Floor:
    def __init__(self,y:int ):
        # No need for an x value, since it spans a lot of values for the floor
        # Instead create a list with all the no or not there positions
        # Create one 'empty' part so that it is easier to keep track off
        # In the middle of the 2 and 3rd screen.
        self.not_blocks = (512, 528)
        # The y takes the height at which the blocks will be created
        self.y = y
