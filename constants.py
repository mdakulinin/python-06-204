#functions and constants
import pygame
from pygame.draw import *

FPS = 30

X = 800
Y = 600

BLUE = (0, 180, 255)
GREEN = (0, 150, 10)
GRAY = (100, 100, 110)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 120, 0)
WHITE = (255, 255, 255)
BROWN = (100, 0, 0)
LEAF = (0, 255, 0)

def sky(screen, color, X, Y):
    rect(screen, color, (0, 0, X, Y // 2))

def grass(screen, color, X, Y):
    rect(screen, color, (0, Y // 2, X, Y // 2))

def house(screen, color_house, color_roof, color_window1, color_window2, x1, y1, x2, y2, h):
    '''
    screen - pygame.display,set_mode object
    x1 - x coordinate of left up angle of the house
    y1 - y coordinate of left up angle of the house
    x2 - x size of the house
    y2 - y size of the rectangle of the house
    h - height of the roof
    color_house - color of the house
    color_roof - color of the roof
    color_window1 - color of the glass in the window
    color_window2 - color of the border
    '''
    BLACK = (0, 0, 0)
    rect(screen, color_house, (x1, y1, x2, y2))
    rect(screen, BLACK, (x1, y1, x2, y2), 2)
    rect(screen, color_window1, (x1 + x2 // 4, y1 + y2 // 4, x2 // 3, y2 // 3))
    rect(screen, color_window2, (x1 + x2 // 4, y1 + y2 // 4, x2 // 3, y2 // 3), 2)
    polygon(screen, color_roof, [(x1, y1), (x1 + x2, y1), (x1 + x2 // 2, y1 - h)])
    polygon(screen, BLACK, [(x1, y1), (x1 + x2, y1), (x1 + x2 // 2, y1 - h)], 2)
    
def cloud(screen, color, x, y, r): 
    '''
    screen - pygame.display,set_mode object
    color - color of the clouds
    x - x coordinate of the center of the leftest part
    y - y coordinate of the center of the leftest part
    r - radius of the parts
    '''
    BLACK = (0, 0, 0)
    for i in range(7):
        if i % 2 == 1:
            circle(screen, color, (x + r * i // 2, y - r // 2), r)
            circle(screen, BLACK, (x + r * i // 2, y - r // 2), r, 1)
        else:
            circle(screen, color, (x + r * i // 2, y + r // 2), r)
            circle(screen, BLACK, (x + r * i // 2, y + r // 2), r, 1)            
            
def palm(screen, color_log, color_leaf, x, y, l, h, r):
    '''
    color_log - color of the log
    color_leaf - color of the leaf
    x - x coordinate of the left up angle of the log
    y - y coordinate of the left up angle of the log
    l - the width of the log
    h - the high of the log
    r - radius of the leaves
    screen - pygame.display,set_mode object
    '''
    BLACK = (0, 0, 0)
    rect(screen, color_log, (x, y, l, h))
    rect(screen, BLACK, (x, y, l, h))
    x1 = x + l // 2
    circle(screen, color_leaf, (x, y), r)
    circle(screen, BLACK, (x, y), r, 1)
    circle(screen, color_leaf, (x + l, y), r)
    circle(screen, BLACK, (x + l, y), r, 1)
    circle(screen, color_leaf, (x + l, y), r)
    circle(screen, BLACK, (x + l, y), r, 1)    
    circle(screen, color_leaf, (x1, y - r), r)
    circle(screen, BLACK, (x1, y - r), r, 1)  
    circle(screen, color_leaf, (x, y - 2 * r), r)
    circle(screen, BLACK, (x, y - 2 * r), r, 1)
    circle(screen, color_leaf, (x + l, y - 2 * r), r)
    circle(screen, BLACK, (x + l, y - 2 * r), r, 1)     
