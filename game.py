import pyxel
from time import time
from backgroud import background
from coin import coin
from utility import box_collides
from game_manager import GameStates, game_manager
from gfxmanager import GfxManager
from player import player
from tube import tube


class Game:

    def __init__(self):
        pyxel.init(160,160,"Flappy Bird made in Python",45)
        GfxManager()
        self.game_manager = game_manager()

        #instances
        self.player = player(pyxel.width*0.3,pyxel.height*0.6,17,13,self.game_manager)
        self.tubeup1 = tube(pyxel.width + 16,32,80,0.2,0.45)
        self.tubedown1 = tube(pyxel.width + 16,32,80,0.2,0.35,True)
        self.tubeup2 = tube(pyxel.width * 1.5 + 16,32,80,0.2,0.45)
        self.tubedown2 = tube(pyxel.width * 1.5 + 16,32,80,0.2,0.35,True)
        self.coin1 = coin(self.tubeup1.x,pyxel.height*0.5,12,16,self.game_manager)
        self.coin2 = coin(self.tubeup2.x,pyxel.height*0.5,12,16,self.game_manager)
        self.game_objects = [self.tubeup1,self.tubedown1,self.tubeup2,self.tubedown2,self.coin1,self.coin2,self.player]

        self.bg = background(90,160,1)

        pyxel.run(self.update,self.draw)

    def update(self):
        self.game_manager.new_frame_time = time()

        if pyxel.btnp(pyxel.KEY_Q): pyxel.quit()

        self.game_states_update()

    def draw(self):
        pyxel.cls(2)

        self.bg.draw()

        for gobj in self.game_objects:
            gobj.draw()

        self.game_states_draw()

    def game_states_update(self):
        if self.game_manager.game_state == GameStates.MENU:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.game_manager.game_state = GameStates.PLAY

        elif self.game_manager.game_state == GameStates.PLAY:
            for gobj in self.game_objects: 
                gobj.update()

            self.coin1.x = self.tubeup1.x
            self.coin2.x = self.tubeup2.x

            self.check_collisions()

            self.game_manager.calculate_frame()

        elif self.game_manager.game_state == GameStates.OVER:
            if pyxel.btn(pyxel.KEY_R):
                self.reset_game()
                self.game_manager.game_state = GameStates.PLAY

    def game_states_draw(self):
        if self.game_manager.game_state == GameStates.MENU:
            text = "PRESS SPACE BUTTON TO START"
            GfxManager.draw_text(pyxel.width*0.5 - len(text)*2,30,text,10) 

        elif self.game_manager.game_state == GameStates.PLAY:
            GfxManager.draw_text(50,20,"ACTUAL SCORE: "+str(self.game_manager.actual_score),10)
            self.bg.update()

        elif self.game_manager.game_state == GameStates.OVER:
            self.game_over()

    def check_collisions(self):
        for this in self.game_objects:
            for other in self.game_objects:
                if this == other: continue

                result = box_collides(this.x,this.y,other.x,other.y,this.width*0.5,other.width*0.5,this.height*0.5,other.height*0.5)

                if result == False:
                    continue
                else:
                     this.on_collide(other)

    def game_over(self):
        text = "GAME OVER"
        GfxManager.draw_text(pyxel.width*0.5 - len(text)*2,30,text,10) 
        text = "YOUR HIGHSCORE: "+ str(self.game_manager.highscore)
        GfxManager.draw_text(pyxel.width*0.5 - len(text)*2,40,text,10) 
        text = "PRESS R TO RESTART"
        GfxManager.draw_text(pyxel.width*0.5 - len(text)*2,50,text,10) 

    def reset_game(self):
        self.player.x = pyxel.width*0.3
        self.player.y = pyxel.height*0.6
        self.player.fall_speed = 0
        self.tubeup1.setRandomY()
        self.tubedown1.setRandomY()
        self.tubeup1.x = pyxel.width + self.tubeup1.width*0.5
        self.tubedown1.x = pyxel.width + self.tubeup1.width*0.5
        self.tubeup2.setRandomY()
        self.tubedown2.setRandomY()
        self.tubeup2.x = pyxel.width * 1.5 + self.tubeup2.width*0.5
        self.tubedown2.x = pyxel.width * 1.5 + self.tubeup2.width*0.5
        self.game_manager.actual_score = 0
        self.coin1.is_active = True
        self.coin2.is_active = True

if __name__ == "__main__":
    Game()