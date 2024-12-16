# import modules
import pygame
import sys

# function for drowing net


def draw_net():
    for i in range(5):
        rectangle = pygame.Rect(i*(screen_width/5), 0,
                                screen_width/10, screen_height)
        pygame.draw.rect(screen, (0, 0, 0), rectangle, width=2)
    for i in range(5):
        rectangle = pygame.Rect(0, i*(screen_height/5),
                                screen_width, screen_height/10)
        pygame.draw.rect(screen, (0, 0, 0), rectangle, width=2)

    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, screen_height), width=20)
    pygame.draw.line(screen, (0, 0, 0), (0, screen_height),
                     (screen_width, screen_height), width=20)
    pygame.draw.line(screen, (0, 0, 0), (screen_width,
                     screen_height), (screen_width, 0), width=20)
    pygame.draw.line(screen, (0, 0, 0), (screen_width, 0), (0, 0), width=20)


# initialization and create window
pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((1000, 1000))
FPS = 10
clock = pygame.time.Clock()

# player cfg
player_height = 100
player_width = 50

posX = 0
posY = 0

player = pygame.transform.scale(pygame.image.load(
    "sprites/walk_right.png"), (player_width, player_height))

# create shadow
shadow = pygame.transform.scale(pygame.image.load("sprites/shadow.png"), (2472, 2262))

# main loop
while True:
    screen.fill((192, 192, 192))
    draw_net()
    screen.blit(player, (posX, posY))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and posX < 900:
        player = pygame.transform.scale(pygame.image.load(
            "sprites/walk_right.png"), (player_width, player_height))
        posX += 100
    if keys[pygame.K_w] and posY > 99:
        player = pygame.transform.scale(pygame.image.load(
            "sprites/walk_top.png"), (player_width, player_height))
        posY -= 100
    if keys[pygame.K_a] and posX > 99:
        player = pygame.transform.scale(pygame.image.load(
            "sprites/walk_left.png"), (player_width, player_height))
        posX -= 100
    if keys[pygame.K_s] and posY < 900:
        player = pygame.transform.scale(pygame.image.load(
            "sprites/walk_down.png"), (player_width, player_height))
        posY += 100

    screen.blit(shadow, (posX-1190,posY-1020))

    # update screen
    pygame.display.update()

    # condition for close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
