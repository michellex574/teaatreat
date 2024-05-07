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

bg = pygame.image.load("bg.jpg")
pancakes_eaten = 0
waffles_eaten = 0
start_time = round(time.time())

# render the text for later
message = "Use the left and right arrow keys to move the food!"
pancakes = "pancakes eaten: " + str(pancakes_eaten)
waffles = "waffles eaten: " + str(waffles_eaten)
end_message = "Time's up! They sure are fed! "
end_message2 = "Time's up! Did you starve them?.. "
end_message3 = "Time's up! They're satisfied now that's for sure! "
display_message = my_font.render(message, True, (0, 0, 0))
display_pancakes = my_font.render(pancakes, True, (255, 255, 255))
display_waffles = my_font.render(waffles, True, (255, 255, 255))
run = True

while run == True:
    current_time = round((time.time() - start_time), 2)
    display_time_elapsed = my_font.render("Time Elapsed: " + str(current_time), True, (255, 255, 255))
    if time == 0:
        run = False
    pygame.display.update()

if waffles_eaten + pancakes_eaten <= 4:
    screen.blit(display_pancakes, (0, 0))
    screen.blit(display_waffles, (0, 5))

pygame.quit()