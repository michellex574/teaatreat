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
c = Cat(270, 180)
shown = random.randint(1,3)
if shown == 1:
    shown = p
elif shown == 2:
    shown = w
r = 178
g = 34
b = 34
background = Background(0 ,0)
pancakes_eaten = 0
waffles_eaten = 0


# render the text for later
message = "Use the a and d keys to move the food!"
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
display_end_message = my_font.render(end_message, True, (0, 0, 0))
display_end_message2 = my_font.render(end_message2, True, (0, 0, 0))
display_end_message3 = my_font.render(end_message3, True, (0, 0, 0))

start_time = time.time()
seconds_elapsed = 1
time_appear = 0

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

     if keys[pygame.K_d] and shown == p:
         p.move_direction("right")

     if keys[pygame.K_a] and shown == p:
         p.move_direction("left")

     if keys[pygame.K_d] and shown == w:
         p.move_direction("right")

     if keys[pygame.K_a] and shown == w:
         p.move_direction("left")

     if b.rect.colliderect(p.rect):
         eaten = "eaten detected"
         display_eaten = my_font.render(eaten, True, (255, 255, 255))
         pancakes = pancakes + 5
         display_score = my_font.render("Pancakes: " + str(pancakes), True, (255, 255, 255))
     elif b.rect.colliderect(w.rect):
         disgust = "disgust detected"
         display_disgust = my_font.render(disgust, True, (255, 255, 255))

     if c.rect.colliderect(w.rect):
         eaten = "eaten detected"
         display_eaten = my_font.render(eaten, True, (255, 255, 255))
         waffles = waffles + 5
         display_score = my_font.render("Waffles: " + str(waffles), True, (255, 255, 255))
     elif c.rect.colliderect(p.rect):
         disgust = "disgust detected"
         display_disgust = my_font.render(disgust, True, (255, 255, 255))

     for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            intro_screen = False
            game_screen = False
            end_screen = False

     if seconds_elapsed >= 0:
        screen.fill((r, g, b))
        screen.blit(background.image, (0, 0))
        screen.blit(display_pancakes, (1, 0))
        screen.blit(display_waffles, (1, 15))
        screen.blit(c.image, c.rect)
        screen.blit(b.image, b.rect)
        screen.blit(p.image, p.rect)
        screen.blit(w.image, w.rect)
        current_time = time.time()
        seconds_elapsed = round((start_time - current_time) + 10, 2)
        countdown = my_font.render("Time Elapsed: " + str(seconds_elapsed) + "s", True, (255, 255, 255))
        screen.blit(countdown, (375, 0))

     else:
        game_screen = False
        end_screen = True

     pygame.display.update()

while end_screen:
    screen.fill((r, g, b))
    if pancakes_eaten > 20:
        display_end_message = my_font.render(end_message, True, (0, 0, 0))
        screen.blit(display_end_message, (175, 165))

    if pancakes_eaten < 5:
        display_end_message2 = my_font.render(end_message2, True, (0, 0, 0))
        screen.blit(display_end_message2, (175, 165))

    if pancakes_eaten > 10 and pancakes_eaten < 15:
        display_end_message2 = my_font.render(end_message3, True, (0, 0, 0))
        screen.blit(display_end_message3, (175, 165))

    if waffles_eaten > 20:
        display_end_message = my_font.render(end_message, True, (0, 0, 0))
        screen.blit(display_end_message, (175, 165))

    if waffles_eaten < 5:
        display_end_message2 = my_font.render(end_message2, True, (0, 0, 0))
        screen.blit(display_end_message2, (175, 165))

    if waffles_eaten > 10 and waffles_eaten < 15:
        display_end_message2 = my_font.render(end_message3, True, (0, 0, 0))
        screen.blit(display_end_message3, (175, 165))

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            intro_screen = False
            game_screen = False
            end_screen = False

    pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()