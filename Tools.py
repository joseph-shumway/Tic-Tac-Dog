import arcade
import time as time


# Create Shape class
class Shape:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class Grid:
    def draw(self):
        arcade.draw_rectangle_outline(111, 111, 222, 222, arcade.color.AIR_FORCE_BLUE),
        arcade.draw_rectangle_outline(111, 333, 222, 222, arcade.color.AIR_FORCE_BLUE),
        arcade.draw_rectangle_outline(111, 555, 222, 222, arcade.color.AIR_FORCE_BLUE),

        arcade.draw_rectangle_outline(333, 111, 222, 222, arcade.color.AIR_FORCE_BLUE),
        arcade.draw_rectangle_outline(333, 333, 222, 222, arcade.color.AIR_FORCE_BLUE),
        arcade.draw_rectangle_outline(333, 555, 222, 222, arcade.color.AIR_FORCE_BLUE),

        arcade.draw_rectangle_outline(555, 111, 222, 222, arcade.color.AIR_FORCE_BLUE),
        arcade.draw_rectangle_outline(555, 333, 222, 222, arcade.color.AIR_FORCE_BLUE),
        arcade.draw_rectangle_outline(555, 555, 222, 222, arcade.color.AIR_FORCE_BLUE)


class FireBox:

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def draw(self, x, y, state):

        arcade.draw_rectangle_filled(x * 111, y * 111, 222, 222,  arcade.color.YELLOW_ORANGE)


    def choose_fire(self):
        print()
