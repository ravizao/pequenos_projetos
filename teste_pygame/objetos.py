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
            self.aresta_central_x=self.arestas_x
            self.arestas_x=self.pos[0]

            self.arestas_width=self.largura_aresta

    def desenhar(self,main ):
        pygame.draw.rect(main.tela,self.cor,self.centro)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_direita)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_central)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_esquerda)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_superior)
        pygame.draw.rect(main.tela,(0,0,0),self.aresta_inferior)







class Texto:
    def __init__(self,texto,cor,x,y,tamanho,input):
        self.tamanho=tamanho
        self.cor=cor
        self.pos_input=(x,y)
        self.font = pygame.font.Font('freesansbold.ttf', self.tamanho)
        self.texto=self.font.render(texto, False, cor)
        self.rect=self.texto.get_rect()
        self.rect.y=y
        self.rect.x=x
        self.input=input
        self.input_str=''
        self.digitando=False




    def desenhar(self,tela):
        tela.blit(self.texto, (self.rect.x, self.rect.y))
        if self.input:
            pygame.draw.rect(tela,self.cor_input,self.input_box)
            tela.blit(self.input_text,(self.input_rect.x,self.input_rect.y))




    def gerar_input(self):
        self.cor_input = (50,50,50) if self.digitando else (0,0,0)
        self.input_box=pygame.Rect(self.pos_input[0],self.pos_input[1]+self.tamanho+5,200,self.tamanho)
        self.input_text=self.font.render(self.input_str, False, self.cor)
        self.input_rect=self.input_text.get_rect()
        self.input_rect.x=self.pos_input[0]+5
        self.input_rect.y=self.pos_input[1]+self.tamanho+5
