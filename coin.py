import pyxel
from game_manager import CollisionType, game_manager
from game_object import game_object
from gfxmanager import GfxManager

class coin(game_object):
    def __init__(self,x,y,width,height,game_manager : game_manager):
        super().__init__(x,y,width,height,CollisionType.COIN,GfxManager.texturesId["tilemap"],18,0)
        self.game_manager = game_manager

    def update(self):
        if self.x < 0 - self.width*0.5 :
            self.x = pyxel.width + self.width*0.5
            self.is_active = True
        self.x -=5

    def on_collide(self,other):
        if self.is_active:
            if other.collision_type == CollisionType.PLAYER:  
                self.game_manager.actual_score +=1
                if self.game_manager.highscore < self.game_manager.actual_score:
                    self.game_manager.highscore = self.game_manager.actual_score
                self.is_active = False