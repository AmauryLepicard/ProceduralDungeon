import sys

import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
area = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# text
myFont30 = pygame.font.SysFont(None, 30)
myFont200 = pygame.font.SysFont(None, 200)
myFont100 = pygame.font.SysFont(None, 100)
pygame.display.set_caption("Procedural Dungeon Generator")

mouseSprite = pygame.sprite.Sprite()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

    # update gameModel
    delta = clock.tick(60)

    # clear screen
    screen.fill((0, 0, 0))

    pygame.display.flip()
