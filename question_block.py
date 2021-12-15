class QuestionBlock:
    def __init__(self, y:int):
        # The initialisation of y allows for the different heights of the blocks
        # This was also meant to be used for normal blocks but straight out wasn't done
        self.y = y
        # This two lists define the placement of the different blocks that will appear throughout the level
        # These are the coordinates of question blocks at height 3 blocks from the floor
        self.bQB3 =[272, 336, 368, 912, 960]
        # The same as the above but at 6 blocks of height
        self.bQB6 = [352]
