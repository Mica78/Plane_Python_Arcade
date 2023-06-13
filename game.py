import arcade
from settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SCREEN_TITLE,
    SCREEN_RESIZABLE,
    PLAYER_MOUVEMENT,
    LAND_SCALE,
    LAND_RANGE
)
from player import Player
from land import Land


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=SCREEN_RESIZABLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.plane_sprite = None
        self.land = None
        self.land_list = None

    def setup(self):
        self.land_list = arcade.SpriteList()

        self.plane_sprite = Player()

        for x in range(0, SCREEN_WIDTH, int(LAND_SCALE * LAND_RANGE)):
            land = Land()
            land.left = x
            self.land_list.append(land)

    def on_draw(self):
        self.clear()
        self.land_list.draw()
        self.plane_sprite.draw()

    def on_key_press(self, key, modifiers):

        if self.plane_sprite.speed > 0:
            if key == arcade.key.W:
                self.plane_sprite.change_angle = -PLAYER_MOUVEMENT
            if key == arcade.key.S:
                self.plane_sprite.change_angle = PLAYER_MOUVEMENT
        if key == arcade.key.ESCAPE:
            if self.plane_sprite.speed == 0:
                self.plane_sprite.speed = 1
            else:
                self.plane_sprite.speed = 0

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W or key == arcade.key.S:
            self.plane_sprite.change_angle = 0

    def update(self, delta_time):
        self.plane_sprite.update()


def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
