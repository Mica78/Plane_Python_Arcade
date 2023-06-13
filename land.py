import arcade
import random

from settings import LAND_IMAGE, LAND_SCALE


class Land(arcade.Sprite):

    def __init__(self):
        super().__init__(LAND_IMAGE, LAND_SCALE)
        self.left = 0
        self.bottom = 0
        self.angle = 0

    def update(self):
        pass
