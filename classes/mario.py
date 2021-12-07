import constant



class Mario:
    def __init__(self, x, y, lives):
        if x > 0:
            self.x = x
        else:
            self.x = 0
        if y > 0:
            self.y = y
        else:
            self.y = 0

        self.lives = lives
        self.speed = 2
        self.jumping = False
        self.image = constant.MARIO_IMAGE
        self.score = 0
        self.jumpcount = 0
        self.jump_height = 10

    #    Here I have two functions, one for the movement sideways and one for the move
    #    ment up and down, because in the first one I just need the attributes
    #    direction(left,right) and the list of platforms to check the postion but in the
    #    other funcion I need also to take as a parameter the list of ladder, plus the two
    #    that I have already said.

    def move_horizontal(self, direction, listBreakableBrickBlock):

        #        This doesn't work yet because I don't know why but what I'm trying is to make
        #        an effective code for the bounds of the platforms such that if Mario is
        #        not on the platform he will fall down to the next one
        #        for i in range(len(listPlatform)):
        #             if (self.x not in range(listPlatform[i].x, listPlatform[i].x + constant.PLATFORM_IMAGE[3])):

        if direction == 'right':
            for i in range(len(listPlatform)):
                if self.y == listPlatform[i].y - constant.MARIO_HEIGHT:
                    self.x += self.speed

        if direction == 'left':
            for i in range(len(listPlatform)):
                if self.y == listPlatform[i].y - constant.MARIO_HEIGHT:
                    self.x -= self.speed

    #        This functions of movement are really simple they just check if Mario is
    #        in the platform

    def move_vertical(self, direction, listPlatform, listLadder):
        if direction == 'up':
            for i in range(len(listPlatform)):
                if i < 5:
                    if ((listPlatform[i].y - constant.MARIO_HEIGHT < self.y <=
                         listPlatform[i + 1].y - constant.MARIO_HEIGHT) and
                            (self.x in range(listLadder[i].x - 5, listLadder[i].x + 5))):
                        self.y -= self.speed

        if direction == 'down':
            for i in range(len(listPlatform) - 1):
                if i < 5:
                    if ((listPlatform[i].y - constant.MARIO_HEIGHT <= self.y <
                         listPlatform[i + 1].y - constant.MARIO_HEIGHT) and
                            (self.x in range(listLadder[i].x - 5, listLadder[i].x + 5))):
                        self.y += self.speed

        elif direction == 'jump':
            while self.jumpcount != -self.jump_height:
                self.y -= 1
                self.x += 1
                self.jumpcount -= 1
        elif self.jumpcount == -self.jump_height:
            while self.jumpcount != 0:
                self.y += 1
                self.x += 1
                self.jumpcount += 1

            #        This functions are the same so I will just explain how one works the other
#        one is a copy and paste. Okey, so you have a for loop that works only if
#        i is less than 5 because if it's 5 you don't one to go further down
#        because it's the last platform, so I say if self.y is in either in between
#        two ramps or in the ramps IF the Mario is really close or in the ladders,
#        that's why here I have as an attribute the list of ladders


#       This is to make him jump but it's not the priority rn


#    This doesn't do shit jet
#    def respawn(self):
#        if self.life == 0:
#            '''Goes back to the initial postition'''
#        self.attempts -= 1
#
#