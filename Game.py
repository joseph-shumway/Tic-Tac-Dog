"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 666
SCREEN_HEIGHT = 666
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 222


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites.
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None
        self.time = None

        arcade.set_background_color(arcade.csscolor.MAROON)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.time = 0

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/tiles/boxCrate_double.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 333
        self.player_sprite.center_y = 333
        self.player_list.append(self.player_sprite)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.player_list.draw()
        arcade.draw_text(str(self.time), 100, 100, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if (key == arcade.key.UP or key == arcade.key.W) and self.player_sprite.center_y + PLAYER_MOVEMENT_SPEED < 666:
            self.player_sprite.center_y = self.player_sprite.center_y + PLAYER_MOVEMENT_SPEED
        elif (
                key == arcade.key.DOWN or key == arcade.key.S) and self.player_sprite.center_y - PLAYER_MOVEMENT_SPEED > 0:
            self.player_sprite.center_y = self.player_sprite.center_y - PLAYER_MOVEMENT_SPEED
        elif (
                key == arcade.key.LEFT or key == arcade.key.A) and self.player_sprite.center_x - PLAYER_MOVEMENT_SPEED > 0:
            self.player_sprite.center_x = self.player_sprite.center_x - PLAYER_MOVEMENT_SPEED
        elif (
                key == arcade.key.RIGHT or key == arcade.key.D) and self.player_sprite.center_x + PLAYER_MOVEMENT_SPEED < 666:
            self.player_sprite.center_x = self.player_sprite.center_x + PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Move the player with the physics engine
        self.physics_engine.update()
        self.time += delta_time


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
