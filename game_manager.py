import pandas as pd
from enum import Enum
from time import time
from file_IO import write_csv_pandas

class GameStates(Enum):
    MENU = 0
    PLAY = 1
    OVER = 2

class CollisionType(Enum):
    NULL = 0
    PLAYER = 1
    TUBE = 2
    COIN = 3

class game_manager():
    def __init__(self,game_state = GameStates.MENU):
        self.gravity = 0.4
        self.game_state = game_state
        self.highscore = 0
        self.actual_score = 0

        self.new_frame_time = time()
        self.old_frame_time = self.new_frame_time
        self.actual_frame_rate = 0
        self.average_frame_rate = 0
        self.frame_rate_data = []
        self.average_frame_rate_data = []
        self.score = []
        self.actual_game = 0
        self.game = []

    def save_data(self):
        average_frame = 0

        for frame_data in self.frame_rate_data:
            average_frame+=frame_data

        average_frame /= len(self.frame_rate_data)

        self.average_frame_rate_data.append(str(average_frame*1000))

        self.actual_game+=1
        self.game.append(str(self.actual_game))

        df = pd.DataFrame(zip(self.game,self.average_frame_rate_data ,self.score),columns=['Game','Average Frame Rate','Score'])
        write_csv_pandas('data3.csv',df)

    def calculate_frame(self):
        self.actual_frame_rate = self.new_frame_time - self.old_frame_time
        self.old_frame_time = self.new_frame_time
        self.frame_rate_data.append(self.actual_frame_rate)
