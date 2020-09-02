import pygame
from pygame.locals import *
import math
from objetos import *






pygame.init()









class Main:
    def __init__(self,tela_x,tela_y,textos,cubos):
        self.tela_x=tela_x
        self.tela_y=tela_y
        self.tela=pygame.display.set_mode((self.tela_x,self.tela_y))
        self.textos=textos
        self.cubos=cubos



        self.background_menu=pygame.Rect(self.tela_x-200,0,200,self.tela_y)

    def mudar_cubo(self,propriedade,cubo,var):
        for i in range(len(self.cubos)):
            if self.cubos[i] == cubo:
                if propriedade=='tamanho':
                    self.cubos[i].largura_aresta=var
                elif propriedade=='x':
                    self.cubos[i].pos[0]=var
                elif propriedade=='y':
                    self.cubos[i].pos[1]=var
                elif propriedade=='velocidade':
                    self.cubos[i].vel_rotacao=var




    def rodar(self):
        pygame.display.set_caption('Formas')
        rodando=True


        while rodando:
            main.tela.fill((255,255,255))



            for cubo in self.cubos:
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
                    for cubo in self.cubos:
                        if cubo.centro.collidepoint(event.pos):
                            for texto in self.textos:
                                texto.get_cubo(cubo)


                    for texto in self.textos:
                        if texto.input and (texto.input_box.collidepoint(event.pos)):
                            # Toggle the active variable.
                            texto.digitando = not texto.digitando
                        else:
                            texto.digitando = False
                if event.type == pygame.KEYDOWN:
                    for texto in self.textos:
                        if texto.digitando:
                            if event.key == pygame.K_RETURN:
                                self.mudar_cubo(texto.str_texto,texto.cubo,float(texto.input_str))
                                texto.input_str = ''
                            elif event.key == pygame.K_BACKSPACE:
                                texto.input_str= texto.input_str[:-1]
                            else:
                                texto.input_str += event.unicode
















cubos=[Cubo(50,300,200,0.4,(255,0,0)),Cubo(50,300,300,0.4,(255,0,0))]
textos=[Texto('tamanho',(0,0,210),810,20,20,True),Texto('x',(0,0,210),810,70,20,True),Texto('y',(0,0,210),810,120,20,True),Texto('velocidade',(0,0,210),810,170,20,True)]


main=Main(1000,600,textos,cubos)

main.rodar()



pygame.quit()
