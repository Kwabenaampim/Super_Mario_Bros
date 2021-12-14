class Pipes:
    def __init__(self, y:int):
        # The y variable will contain the maximum height of the pipe
        # Which will draw the other pipes by reducing theiri height byt he pixels needed
        self.y = y
        # the pipes class serves for the purpose of containing the list of the positions they will be at
        # PLus the different heights
        self.pipes_list = [432, 592]
        # Later on, in the board file I'll add the different conditionals
        # That will draw the different heights of the pipe
