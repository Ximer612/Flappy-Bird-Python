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

        random_y = 16

        super().__init__(x,random_y,width,height,CollisionType.TUBE,GfxManager.texturesId["tube"])

        if not isSecond :
            super().__init__(x,randint(pyxel.height-height *self.resetDown,pyxel.height+height *self.resetUp),width,height,CollisionType.TUBE,GfxManager.texturesId["tube"])
        else:
            super().__init__(x,randint(-height *0.5,height *0.5),width,height,CollisionType.TUBE,GfxManager.texturesId["tube"])

    def update(self):
        if self.x < 0 - self.width*0.5 :
            self.x = pyxel.width + self.width*0.5
            self.setRandomY()
        self.x -=5

    def setRandomY(self):

        if not self.isSecond :
            self.y = randint(pyxel.height-self.height *self.resetDown,pyxel.height+self.height *self.resetUp)
        else:
            self.y = randint(-self.height *self.resetDown,self.height *self.resetUp)

    def draw(self):
        if not self.isSecond :
            super().draw()
        else:
            super().draw(1,-1)



