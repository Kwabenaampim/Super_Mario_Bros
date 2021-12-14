# here it is to be renamed as Mario when the jump movement is implemented
class MARIO():
    def __init__(self, x:int, y:int, dir:bool ):
        self.x = x
        self.y = y
        self.moved_middle=0
        self.decrease = 0
        self.direction = dir
        #self.sprite =(0,0) # Later to be susbtituted byt the tuple in Constants folder
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
        
        # How to make it 'fall' once the player has reached certain height
        if direction.lower() == 'up' and self.y < size - mario_y_size:
            if self.y > 154:
                self.y -= 8
        elif direction.lower()== 'down' and self.y < 224:
            self.y += 2
        # How do I add the effect of gravity?
