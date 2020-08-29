import pygame
from pygame.locals import *
import math

pygame.init()


class Main:
    def __init__(self,tela_x,tela_y):
        self.tela_x=tela_x
        self.tela_y=tela_y
        self.tela=pygame.display.set_mode((self.tela_x,self.tela_y))



class Cubo:
    def __init__(self,aresta,x,y,vel_rotacao,cor):
        self.pos=(x,y)
        self.aresta=aresta
        self.t_aresta_x=aresta
        self.t_aresta_y=aresta
        self.x=x
        self.y=y
        self.x_aresta_central=x
        self.y_aresta_central=y
        self.hipotenusa=math.sqrt((aresta**2)+(aresta**2))
        self.vel_rotacao=vel_rotacao
        self.figura_grow=((aresta/2)/vel_rotacao)/((self.hipotenusa-aresta)/(vel_rotacao*0.1))
        self.cores=[cor,(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

    def gerar_figuras(self):
        centro=pygame.Rect(self.x,self.y,self.t_aresta_x,self.t_aresta_y)
        aresta_central=pygame.Rect(self.x_aresta_central,self.y_aresta_central,2,self.t_aresta_y)
        aresta_esquerda=pygame.Rect(self.x,self.y,2,self.t_aresta_y)
        aresta_direita=pygame.Rect(self.x+self.t_aresta_x-1,self.y,2,self.t_aresta_y)
        aresta_superior=pygame.Rect(self.x,self.y,self.t_aresta_x,2)
        aresta_inferior=pygame.Rect(self.x,self.y+self.t_aresta_y-2,self.t_aresta_x,2)

        self.rects=[centro,aresta_central,aresta_esquerda,aresta_direita,aresta_superior,aresta_inferior]

    def rodar(self):
        self.x_aresta_central+=self.vel_rotacao
        if self.x_aresta_central<self.pos[0]+(self.aresta/2):
            self.t_aresta_x+=self.figura_grow
            self.x-=self.figura_grow/2
        if self.x_aresta_central>=self.pos[0]+(self.aresta/2):
            self.t_aresta_x-=self.figura_grow
            self.x+=self.figura_grow/2
        if self.x_aresta_central>=self.pos[0]+self.aresta:
            self.x_aresta_central=self.pos[0]
            self.x=self.pos[0]
            self.t_aresta_x=self.aresta



main=Main(800,600)
cubos=[Cubo(50,350,250,0.1,(255,0,0)),Cubo(75,50,50,0.1,(255,255,255)),Cubo(30,30,500,0.1,(0,255,0)),Cubo(100,650,250,0.5,(0,0,255)),Cubo(14,600,50,0.1,(255,255,0)),Cubo(87,650,150,0.1,(139,69,19))]



rodando=True
while rodando:
    main.tela.fill((255,255,255))
    for cubo in cubos:
        cubo.gerar_figuras()
        for i in range(len(cubo.rects)):
            pygame.draw.rect(main.tela,cubo.cores[i],cubo.rects[i])
        cubo.rodar()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando=False


pygame.quit()
