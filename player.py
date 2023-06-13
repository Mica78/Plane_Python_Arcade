import arcade
import math
from settings import PLAYER_IMAGE, PLAYER_IMAGE_SCALING, PLAYER_MOUVEMENT


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__(PLAYER_IMAGE, PLAYER_IMAGE_SCALING, flipped_horizontally=180)
        self.center_x = 200
        self.center_y = 200
        self.speed = 0

    def update(self):
        angle_rad = math.radians(self.angle)
        self.angle += self.change_angle

        self.center_y += self.speed * math.sin(angle_rad)
        self.center_x += self.speed * math.cos(angle_rad)
