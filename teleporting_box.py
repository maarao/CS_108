from designer import *
import random
from dataclasses import dataclass

@dataclass
class World:
    box: DesignerObject
    message: DesignerObject
    score: int
    timer: int

# The score you need to win the game
WIN_THRESHOLD = 5
# The number of updates before the game should end
#    30 updates per second, for 10 seconds
LENGTH_OF_GAME = 30 * 10

def create_the_world() -> World:
    """
    Create a new World with a 20x30 black rectangle inside.
    """
    return World(rectangle("black", 200, 100),
                 text("black", "Score:"),
                 0,
                 0)

def spin_the_box(world: World):
    """
    Increase the world's box angle by one degree, spinning the box a small amount.
    """
    world.box.angle += 1

# def move_the_box(world: World, x: int, y: int):
#     """
#     Move the box to the given position.
#     """
#     world.box.x = x
#     world.box.y = y

def teleport_the_box(world: World):
    """
    Move the box to a random position
    """
    # Have a 1 in 10 chance of jumping around
    if random.randint(0, 9) == 0:
        # Set x/y to be random coordinates within the bounds of the
        # window, given by get_width() and get_height()
        world.box.x = random.randint(0, get_width())
        world.box.y = random.randint(0, get_height())

def track_the_score(world: World):
    """ Keep the message in sync with the current score """
    # Get the current score
    score = world.score
    # Update the message's text based on the score
    world.message.text = "Score: " + str(score)

def check_box_clicked(world: World, x: int, y: int):
    """ Check if the box has been clicked and increase the score """
    # Use the Designer function colliding to check if two objects or
    # an object and a point are colliding.
    if colliding(world.box, x, y):
        # Update the score on a successful click
        world.score += 1

def advance_the_timer(world: World):
    """ Advance the timer by one step """
    world.timer += 1

def the_timer_runs_out(world: World):
    """ Check if the score is above the threshold """
    return world.timer >= LENGTH_OF_GAME

def flash_game_over(world: World):
    """ Flash a game over message """
    if world.score >= WIN_THRESHOLD:
        world.message.text = "Game over, you won!"
    else:
        world.message.text = "Game over, you lose!"

# This tells Designer to call our `create_the_world` function
# when the game starts, in order to setup our initial World.
when("starting", create_the_world)
# Tell Designer to call our spin_the_box function every update.
# There are usually 30 updates per second!
when("updating", spin_the_box)
# # Tell Designer to call our move_the_box function every click.
# when("clicking", move_the_box)
# Tell Designer to call teleport_the_box every update.
when("updating", teleport_the_box)
# Tell Designer to call track_the_score every update.
when("updating", track_the_score)
# Tell Designer to call check_box_clicked when the mouse is clicked
when('clicking', check_box_clicked)
# Tell Designer to update the timer
when('updating', advance_the_timer)
# Tell Designer to check if the game is over, then flash our message
# and pause on that screen
when(the_timer_runs_out, flash_game_over, pause)

start()