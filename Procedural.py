import random
import math
import pygame
import numpy as np

TILE_SIZE = 16
GRID_WIDTH = 100
GRID_HEIGHT = 40


def getRandomPointInCircle(radius):
    u = random.random() + random.random()
    r = u if u < 1 else 2 - u
    theta = random.uniform(0.0, 2 * math.pi)
    return r * radius * math.cos(theta), r * radius * math.sin(theta)


def generateRoom(width, height):
    w = int(width * np.clamp(random.gauss(1, 0.25), 0.5, 2.0))
    h = int(height * np.clamp(random.gauss(1, 0.25), 0.5, 2.0))
    x, y = getRandomPointInCircle(1.0)
    r = pygame.Rect(0, 0, w, h)
    r.centerx = int(x * GRID_WIDTH + GRID_WIDTH / 2)
    r.centery = int(y * GRID_HEIGHT + GRID_HEIGHT / 2)
    return r

def generateRooms(nbRooms):
    roomList=[]
    for i in range(nbRooms):
        r = Room()
        roomList.append(r)

class Room(pygame.sprite.Sprite):
    def __init__(self, maxSize, gridWidth, gridHeight):
        self.rect = generateRoom(GRID_WIDTH / 10, GRID_HEIGHT / 10)
        print(self.rect)
