# here it is to be renamed as Mario when the jump movement is implemented
class MARIO():
    def __init__(self, x:int, y:int, dir:bool):
        # x is the starting point of Mario and y the height at which mario spawns
        self.x = x
        self.y = y
        # The moved_middle was meant to be a distance tracker variable
        # That would have allowed for a rudimentary collision system
        # but it would stop working once the coordinates exceeded the middle of the
        # screen
        self.moved_middle=0
        # This variable is used to make the objects move once mario is 'locked'
        # in the middle of the screen
        self.decrease = 0
        # This two variables where straight out copied from the class example
        # Meant to be used for animation and tracking the amount of lives of Mario
        self.direction = dir
        self.lives = 3
    def move(self, direction:str, size:int):
        mario_x_size = 16
        mario_y_size = 16
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            # Later to be substituted by player speed
            if (self.x+mario_x_size) > size/2:
                self.x = self.x + 0
                self.moved_middle += 2
                if self.moved_middle % 16:
                    self.decrease +=2 # In OOP it has to be like this so 2 is updated every instance, in the other way it only gets once and not again
            else:
                self.x += 2
        elif direction.lower() == 'left':
            # I am assuming that if it is not right it will be left
            self.x = max(self.x-2, 0) # The same here as if right
        
        # The following two act as the vertical movement tracker of Mario
        if direction.lower() == 'up' and self.y < size - mario_y_size:
            if self.y > 154:
                self.y -= 8
        # This is so that once down the sprite starts to fall down
        # Although we are missing something for if the player keeps pressing 'up'
        # It will stay up
        elif direction.lower()== 'down' and self.y < 224:
            self.y += 2
