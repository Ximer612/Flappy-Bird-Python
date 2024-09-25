import pyxel
from game_manager import CollisionType, GameStates, game_manager
import utility
from game_object import game_object
from gfxmanager import GfxManager

class player(game_object):
    def __init__(self,x,y,width,height,game_manager : game_manager):
        super().__init__(x,y,width,height,CollisionType.PLAYER, GfxManager.texturesId["tilemap"],0,0)
        self.jump_force = -game_manager.gravity * 8
        self.fall_speed = 0
        self.game_manager = game_manager

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE): self.fall_speed = self.jump_force

        self.fall_speed += self.game_manager.gravity

        self.y += self.fall_speed

        self.x = utility.clamp(self.x,0,pyxel.width)
        self.y = utility.clamp(self.y,0,pyxel.height)

    def on_collide(self,other):

        if other.collision_type == CollisionType.TUBE:
            self.game_manager.game_state = GameStates.OVER
            self.game_manager.score.append(self.game_manager.actual_score)
            self.game_manager.save_data()
