import pygame
# from simple_pid import *

window_width = 1000
window_height = 1000

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
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

y, vel_y = player.rect.bottom, 0
vel = 5
acceleration = 0.5
gravity = 0.5

# set_point = 500 - player_size * 2

# PID tuning:
# pid = PID(0.035, 0, 0.01, setpoint=set_point)
#pid = PID(0.005, 0, 0.005, setpoint=set_point)

control = 0 # Manual

platforms = []
platformx = 100

def create_rect():
        thisrect = pygame.draw.rect(window, (0, 255, 0), (platformx, 100, 500, 50))
        platforms.append(thisrect)

run = True
while run:
    clock.tick(100)
    acc_y = gravity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  
    position = lava_y - player.rect.centery

    # MANUAL CONTROL 
    if control == 0:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            acc_y = -acceleration
        elif keys[pygame.K_DOWN]:
            acc_y = +5*acceleration

    if keys[pygame.K_m]:
        control = 0
    elif keys[pygame.K_p]:
        control = 1

    # PID CONTROL
    # elif control == 1:
    #     output = pid(position)
    #     if output > 0:
    #         acc_y = -output



    player.rect.centerx = (player.rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % window_width
    
    vel_y += acc_y
    y += vel_y
    
    if y > lava_y:
        player.rect.centerx = startx
        y = starty
        vel_y = 0
        acc_y = 0



    startplatformy = starty
    startplatformx = 0
    startplatformw = 100
    startplatformh = 50

    if player.rect.centerx < startplatformx + startplatformw + 10 and player.rect.centerx > startplatformx - 10:
        if y > startplatformy and y < startplatformy + startplatformh:
            y = starty
            vel_y = 0
            acc_y = 0

    # if keys[pygame.K_LEFTBRACKET]:
    #     print("[")
    for p in platforms:
        p.centerx = (p.centerx + (keys[pygame.K_RIGHTBRACKET]- keys[pygame.K_LEFTBRACKET]) * vel) % window_width
                
    

    player.rect.bottom = round(y)

    window.fill((0, 0, 64))
    pygame.draw.rect(window, (255, 165, 0), (0, lava_y, window_width, 100))
    pygame.draw.rect(window, (0, 0, 255), (startplatformx, startplatformy, startplatformw, startplatformh))
    create_rect()
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
exit() 


'''
floor is lava



array of platforms - for i in {arrayname}:
                        move left x pixels
'''
