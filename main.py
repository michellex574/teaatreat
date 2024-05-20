import pygame
import random
import time
from bunny import Bunny
from cat import Cat
from pancake import Pancake
from background import Background
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

pancake = Pancake(180, 205)
waffle = Waffle(180, 205)
bunny = Bunny(80, 205)
cat = Cat(280, 220)
shown = random.randint(1,3)
if shown == 1:
    shown = pancake
elif shown == 2 or shown == 3:
    shown = waffle
r = 178
g = 34
b = 34
background = Background(0, 0)
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
display_pancake_score = my_font.render(pancakes, True, (0, 0, 0))
display_waffle_score = my_font.render(waffles, True, (0, 0, 0))
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

     if keys[pygame.K_d] and shown == pancake:
         pancake.move_direction("right")

     if keys[pygame.K_a] and shown == pancake:
         pancake.move_direction("left")

     if keys[pygame.K_w] and shown == pancake:
         pancake.move_direction("up")

     if keys[pygame.K_s] and shown == pancake:
         pancake.move_direction("down")

     if keys[pygame.K_d] and shown == waffle:
         waffle.move_direction("right")

     if keys[pygame.K_a] and shown == waffle:
         waffle.move_direction("left")

     if keys[pygame.K_w] and shown == waffle:
         waffle.move_direction("up")

     if keys[pygame.K_s] and shown == waffle:
         waffle.move_direction("down")


     if bunny.rect.colliderect(pancake.rect):
         message = "Collision detected"
         display_message = my_font.render(message, True, (0, 0, 0))
         new_x = random.randint(15, 375)
         new_y = random.randint(15, 225)
         pancake.set_location(new_x, new_y)
         pancakes_eaten = pancakes_eaten + 1

     if bunny.rect.colliderect(pancake.rect):
         pancakes_eaten += 1
         pancakes = "pancakes eaten: " + str(pancakes_eaten)
         display_pancake_score = my_font.render(pancakes, True, (0, 0, 0))
         shown = random.randint(1, 3)
         if shown == 1:
             shown = pancake
         elif shown == 2 or shown == 3:
             shown = waffle
     # elif bunny.rect.colliderect(waffle.rect):
     #     disgust = "disgust detected"
     #     display_disgust = my_font.render(disgust, True, (0, 0, 0))
     #     display_score = my_font.render(pancakes, True, (0, 0, 0))

     if cat.rect.colliderect(waffle.rect):
         waffles_eaten = waffles_eaten + 1
         waffles = "waffles eaten: " + str(waffles_eaten)
         display_waffle_score = my_font.render(waffles, True, (0, 0, 0))
         shown = random.randint(1, 3)
         if shown == 1:
             shown = pancake
         elif shown == 2 or shown == 3:
             shown = waffle
     # elif cat.rect.colliderect(pancake.rect):
     #     disgust = "disgust detected"
     #     display_disgust = my_font.render(disgust, True, (0, 0, 0))
     #     display_score = my_font.render(waffles, True, (0, 0, 0))


     for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            intro_screen = False
            game_screen = False
            end_screen = False

     if seconds_elapsed >= 0:
        screen.fill((r, g, b))
        screen.blit(background.image, (0, 0))
        screen.blit(display_pancake_score, (5, 0))
        screen.blit(display_waffle_score, (5, 15))
        screen.blit(cat.image, cat.rect)
        screen.blit(bunny.image, bunny.rect)
        if shown == pancake:
          screen.blit(pancake.image, pancake.rect)
        elif shown == waffle:
          screen.blit(waffle.image, waffle.rect)
        current_time = time.time()
        seconds_elapsed = round((start_time - current_time) + 20, 2)
        countdown = my_font.render("Time Elapsed: " + str(seconds_elapsed) + "s", True, (0, 0, 0))
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
        screen.blit(display_end_message, (175, 145))

    if waffles_eaten < 5:
        display_end_message2 = my_font.render(end_message2, True, (0, 0, 0))
        screen.blit(display_end_message2, (175, 145))

    if waffles_eaten > 10 and waffles_eaten < 15:
        display_end_message2 = my_font.render(end_message3, True, (0, 0, 0))
        screen.blit(display_end_message3, (175, 145))

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            intro_screen = False
            game_screen = False
            end_screen = False

    pygame.display.update()
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()