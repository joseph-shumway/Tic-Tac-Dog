"""
Platformer Game
"""
import arcade
import time as time

# Constants
SCREEN_WIDTH = 666
SCREEN_HEIGHT = 666
SCREEN_TITLE = "Tic-Tac-Dog"


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

class fireCubes:
   def choose_fire(self):
       print()


# begin game
class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.BLACK)
        self.grid = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.grid = Grid()

        #

        # self.fireCubes.choose_fire()


        # pass

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        self.grid.draw()

        arcade.draw_text(str((time.time() * 1000) % 100), 123, 405, arcade.color.WHITE, 12)
