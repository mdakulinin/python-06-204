import pygame
from pygame.draw import *
from constants import *


pygame.init()

screen = pygame.display.set_mode((X, Y))

sky(screen, BLUE, X, Y)
grass(screen, GREEN, X, Y)
house(screen, GRAY, RED, BLUE, ORANGE, 100, 250, 200, 150, 50)
cloud(screen, WHITE, 350, 100, 40)
palm(screen, BROWN, LEAF, 591, 227, 23, 100, 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True