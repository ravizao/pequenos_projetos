import pygame
from pygame.locals import *
import math

pygame.init()


tela=pygame.display.set_mode((800,600))


tx=50
cobra_x=350
cobra_y=250
x=cobra_x
y=cobra_y
jogando=True
hip=math.sqrt((50*50)+(50*50))
gspeed=250/((hip-50)*100)
print(gspeed)

while jogando:
    tela.fill((255,255,255))
    pygame.draw.rect(tela,(0,0,255),(cobra_x,cobra_y,tx,50))
    pygame.draw.rect(tela,(0,0,0),(x,y,2,50))
    pygame.draw.rect(tela,(0,0,0),(cobra_x,cobra_y,2,50))
    pygame.draw.rect(tela,(0,0,0),(cobra_x+tx-1,cobra_y,2,50))
    pygame.draw.rect(tela,(0,0,0),(cobra_x,cobra_y,tx,2))
    pygame.draw.rect(tela,(0,0,0),(cobra_x,cobra_y+48,tx,2))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando=False
    x+=0.1
    if x<375:
        tx+=gspeed
        cobra_x-=gspeed/2
    if x>=375:
        tx-=gspeed
        cobra_x+=gspeed/2
    if x>=400:
        x=350
        cobra_x=350
        tx=50



pygame.quit()
