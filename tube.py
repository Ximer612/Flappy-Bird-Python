import pyxel
from random import randint
from game_manager import CollisionType
from game_object import game_object
from gfxmanager import GfxManager

class tube(game_object):
    def __init__(self,x,width,height,resetDown,resetUp,isSecond=False):

        self.isSecond = isSecond
        self.resetDown = resetDown
        self.resetUp = resetUp

        if not isSecond :
            random_y = randint(int(pyxel.height-height *self.resetDown),int(pyxel.height+height *self.resetUp))
        else:
            random_y = randint(-height // 2,height // 2)

        super().__init__(x,random_y,width,height,CollisionType.TUBE,GfxManager.texturesId["tube"])

    def update(self):
        if self.x < 0 - self.width*0.5 :
            self.x = pyxel.width + self.width*0.5
            self.setRandomY()
        self.x -= 5

    def setRandomY(self):

        if not self.isSecond :
            self.y = randint(int(pyxel.height-self.height *self.resetDown),int(pyxel.height+self.height *self.resetUp))
        else:
            self.y = randint(int(-self.height *self.resetDown),int(self.height *self.resetUp))

    def draw(self):
        if not self.isSecond :
            super().draw()
        else:
            super().draw(1,-1)



