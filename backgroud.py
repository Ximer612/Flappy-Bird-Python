import pyxel
from math import ceil
from game_manager import CollisionType
from game_object import game_object
from gfxmanager import GfxManager

class background(game_object):
    def __init__(self,width,height,speed):
        super().__init__(pyxel.width,pyxel.height*0.5,width,height,CollisionType.NULL,GfxManager.texturesId["city"])
        self.num_bg = ceil((pyxel.width/width))
        self.speed = speed

    def update(self):
        if self.x < 0 - self.width*0.5 :
            self.x = pyxel.width
        self.x -= self.speed

    def draw(self):

        temp_num_bg = -self.num_bg

        for i in range(self.num_bg*2 + 1):
             pyxel.blt(self.x + self.width * temp_num_bg, self.y-self.height*0.5, self.textureId, self.u, self.v, self.width, self.height,13)
             temp_num_bg +=1
