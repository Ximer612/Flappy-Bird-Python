import pyxel
from game_manager import CollisionType

class game_object:
    def __init__(self,x,y,width,height,collision_type : CollisionType,textureId,u=0,v=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collision_type = collision_type
        self.textureId = textureId
        self.is_active = True
        self.u = u
        self.v = v

    def update(self):
        pass

    def draw(self,multyw=1,multyh=1):
        if(self.is_active):
            pyxel.blt(self.x-self.width*0.5, self.y-self.height*0.5, self.textureId, self.u, self.v, self.width*multyw, self.height*multyh,13)
            #pyxel.rect(self.x,self.y,1,1,8) ##draw debug pivot

    def on_collide(self,other):
        pass


