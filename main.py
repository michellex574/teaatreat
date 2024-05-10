import pygame
import random
import time
from bunny import Bunny
from cat import Cat
from pancake import Pancake
from bg import Background
from waffle import Waffle

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Tea a Treat")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

p = Pancake(180, 180)
w = Waffle(180, 180)
b = Bunny(90, 180)
r = 178
g = 34
b = 34
background = Background(0 ,0)
pancakes_eaten = 0
waffles_eaten = 0
start_time = round(time.time())


# render the text for later
message = "Use the left and right arrow keys to move the food!"
message2 = "The pancakes are for the bunny!"
message3 = "The waffles are for the fox!"
message4 = "Both the bunny and the fox enjoys the paffle, so it's up to you! "
message5 = "1 paffle = 5 pancakes or 5 waffles"
pancakes = "pancakes eaten: " + str(pancakes_eaten)
waffles = "waffles eaten: " + str(waffles_eaten)
end_message = "Time's up! They sure are fed! "
end_message2 = "Time's up! Did you starve them?.. "
end_message3 = "Time's up! They're satisfied now that's for sure! "
display_message = my_font.render(message, True, (0, 0, 0))
display_message2 = my_font.render(message2, True, (0, 0, 0))
display_message3 = my_font.render(message3, True, (0, 0, 0))
display_message4 = my_font.render(message4, True, (0, 0, 0))
display_message5 = my_font.render(message5, True, (0, 0, 0))
display_pancakes = my_font.render(pancakes, True, (255, 255, 255))
display_waffles = my_font.render(waffles, True, (255, 255, 255))
run = True
intro_screen = True
game_screen = False
end_screen = False


# -------- Main Program Loop -----------
while intro_screen:
    screen.fill((r, g, b))
    screen.blit(display_message, (70, 120))
    screen.blit(display_message2, (70, 145))
    screen.blit(display_message3, (70, 170))
    screen.blit(display_message4, (70, 195))
    screen.blit(display_message5, (70, 220))

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            game_screen = False
            intro_screen = False
            end_screen = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            intro_screen = False
            game_screen = True

    pygame.display.update()

while game_screen:

     keys = pygame.key.get_pressed()  # checking pressed keys

     if keys[pygame.K_d]:
         p.move_direction("right")

     if keys[pygame.K_a]:
         p.move_direction("left")

     if keys[pygame.K_LEFT]:
         p.move_direction("left")

     if keys[pygame.K_RIGHT]:
         p.move_direction("right")

     if b.rect.colliderect(p.rect):
         eaten = "eaten detected"
         display_eaten = my_font.render(eaten, True, (255, 255, 255))
         pancakes = pancakes + 5
         display_score = my_font.render("Pancakes: " + str(pancakes), True, (255, 255, 255))
     elif b.rect.colliderect(w.rect):
         disgust = "disgust detected"
         display_disgust = my_font.render(disgust, True, (255, 255, 255))
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