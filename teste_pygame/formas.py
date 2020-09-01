import pygame
from pygame.locals import *
import math

class Cubo:
    def __init__(self,aresta,x,y,vel_rotacao,cor):
        self.largura_aresta=aresta
        self.grossura_aresta=(self.largura_aresta//50)+1
        self.pos=(x,y)
        self.hipotenusa=math.sqrt((aresta**2)+(aresta**2))
        self.vel_rotacao=vel_rotacao
        self.figura_grow=(self.hipotenusa-aresta)/((aresta/2)/self.vel_rotacao)
        self.cor=cor

        self.aresta_central_x=self.pos[0]
        self.arestas_x=self.pos[0]
        self.arestas_width=self.largura_aresta


    def gerar_rects(self):
        self.centro=pygame.Rect(self.arestas_x,self.pos[1],self.arestas_width,self.largura_aresta)
        self.aresta_central=pygame.Rect(self.aresta_central_x,self.pos[1],self.grossura_aresta,self.largura_aresta)
        self.aresta_esquerda=pygame.Rect(self.arestas_x,self.pos[1],self.grossura_aresta,self.largura_aresta)
        self.aresta_direita=pygame.Rect(self.arestas_x+self.arestas_width-self.grossura_aresta,self.pos[1],self.grossura_aresta,self.largura_aresta)
        self.aresta_superior=pygame.Rect(self.arestas_x,self.pos[1],self.arestas_width,self.grossura_aresta)
        self.aresta_inferior=pygame.Rect(self.arestas_x,self.pos[1]+self.largura_aresta-1,self.arestas_width,self.grossura_aresta)


    def rodar(self):
        self.aresta_central_x+=self.vel_rotacao


        if self.aresta_central.x<self.pos[0]+(self.largura_aresta/2):
            self.arestas_x-=self.figura_grow/2
            self.arestas_width+=self.figura_grow

        if self.aresta_central.x>=self.pos[0]+(self.largura_aresta/2):
            self.arestas_x+=self.figura_grow/2

            self.arestas_width-=self.figura_grow


        if self.aresta_central.x>=self.pos[0]+self.largura_aresta:
            self.aresta_central_x=self.pos[0]
            self.arestas_x=self.pos[0]

            self.arestas_width=self.largura_aresta

    def desenhar(self,main ):
        pygame.draw.rect(main.tela,self.cor,self.centro)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_direita)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_central)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_esquerda)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_superior)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_inferior)
