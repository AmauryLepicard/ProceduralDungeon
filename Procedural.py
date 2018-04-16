import random
import math


def getRandomPointInCircle():
    radius = random.uniform(0.0, 1.0)
    theta = random.uniform(0.0, 2 * math.pi)
    return radius * math.cos(theta), radius * math.sin(theta)

def generateRoom(size):
    w = random.normal(scale=size)
    y = random.normal(scale=size)