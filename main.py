import pygame
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Feast for Tea")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 219
g = 215
b = 210
clicks = 0

# render the text for later
message = "Use the left and right arrow keys to move the food!"
pancakes = "pancakes eaten: "
waffles = "waffles eaten: "
end_message = "Time's up! They sure are fed! "
end_message2 = "Time's up! Did you starve them?.. "
end_message3 = "Time's up! They're satisfied now that's for sure! "
display_message = my_font.render(message, True, (0, 0, 0))
start_time = time.time()
