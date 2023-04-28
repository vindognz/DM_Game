import pygame; from random import *

window_width = 1000
window_height = 1000

pygame.init()
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
clock = pygame.time.Clock()
lava_y = window_height - 50

starty = window_height / 2
startx = 50 - window_width

player = pygame.sprite.Sprite()
player.image = pygame.Surface((30, 30), pygame.SRCALPHA)
player_size = 15
pygame.draw.circle(player.image, (255, 0, 0), (player_size, player_size), player_size)
player.rect = player.image.get_rect(center = (150, lava_y - player_size))
all_sprites = pygame.sprite.Group([player])

pygame.mouse.set_visible(0)

y, vel_y = player.rect.bottom, 0
vel = 5
acceleration = 10
gravity = 0.25
inCollision = True

platforms = []

def create_rect(r, g, b, topleftx, toplefty, width, height):
        thisrect = pygame.draw.rect(window, (r, g, b), (topleftx, toplefty, width, height))
        platforms.append(thisrect)

run = True
while run:
    clock.tick(100)
    acc_y = gravity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  

    if keys[pygame.K_SPACE] or keys[pygame.K_UP] and inCollision == True:
        acc_y = -acceleration
        inCollision = False

    

    player.rect.centerx = (player.rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % window_width
    
              
    
    vel_y += acc_y
    y += vel_y
    


    if y > lava_y:
        player.rect.centerx = startx
        y = starty
        vel_y = 0
        acc_y = 0



    player.rect.bottom = round(y)

    sky_colour = 37, 150, 190
    lava_colour = 255, 102, 0

    window.fill((sky_colour))
    pygame.draw.rect(window, (lava_colour), (0, lava_y, window_width, 100))



    if player.rect.collidelistall(platforms):
        vel_y = -0.5
        acc_y = -0.5
        inCollision = True



    # MISC RANDOM LIGHT BLUE PLATFORM
    create_rect(0, 250, 245, 450, starty - 300, 350, 50)

    # MISC RANDOM TURQUOISE PLATFORM
    create_rect(52, 235, 168, 300, starty - 150, 500, 50)

    # MISC RANDOM GREEN PLATFORM
    create_rect(0, 255, 0, 150, starty, 650, 50)

    # START PLATFORM
    create_rect(0, 0, 255, 0, starty, 100, 50)
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit() 


'''
floor is lava



array of platforms - for i in {arrayname}:
                        move left x pixels
'''
