import pygame
from pygame.locals import *
import math
from formas import *






pygame.init()

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







class Main:
    def __init__(self,tela_x,tela_y):
        self.tela_x=tela_x
        self.tela_y=tela_y
        self.tela=pygame.display.set_mode((self.tela_x,self.tela_y))
        self.textos=()



        self.background_menu=pygame.Rect(self.tela_x-200,0,200,self.tela_y)

















main=Main(1000,600)
cubos=[Cubo(50,700,500,0.4,(255,0,0)),Cubo(75,50,50,0.6,(255,255,255)),Cubo(130,30,400,0.3,(0,255,0)),Cubo(100,650,250,0.5,(0,0,255)),Cubo(100,600,50,0.1,(255,255,0)),Cubo(87,650,150,0.2,(139,69,19))]
textos=[Texto("testando menu",(210,0,0),810,50,20,True)]

pygame.display.set_caption('Formas')
rodando=True


while rodando:
    main.tela.fill((255,255,255))



    for cubo in cubos:
        cubo.gerar_rects()
        cubo.desenhar(main)
        cubo.rodar()

    pygame.draw.rect(main.tela,(0,0,80),main.background_menu)
    for texto in textos:
        if texto.input:
            texto.gerar_input()

        texto.desenhar(main.tela)



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            for texto in textos:
                if texto.input and (texto.input_box.collidepoint(event.pos)):
                    # Toggle the active variable.
                    texto.digitando = not texto.digitando
                else:
                    texto.digitando = False
        if event.type == pygame.KEYDOWN:
            for texto in textos:
                if texto.digitando:
                    if event.key == pygame.K_RETURN:
                        print(texto.input_str)
                        texto.input_str = ''
                    elif event.key == pygame.K_BACKSPACE:
                        texto.input_str= texto.input_str[:-1]
                    else:
                        texto.input_str += event.unicode




pygame.quit()
