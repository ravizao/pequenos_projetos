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
                            self.textos.append(Texto(str(cubo.largura_aresta),(0,0,210),810,textos[len(textos)-1].pos_input[1]+25,20,False))
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
                                print(texto.input_str)
                                texto.input_str = ''
                            elif event.key == pygame.K_BACKSPACE:
                                texto.input_str= texto.input_str[:-1]
                            else:
                                texto.input_str += event.unicode
















cubos=[Cubo(50,700,500,0.4,(255,0,0)),Cubo(75,50,50,0.6,(255,255,255)),Cubo(130,30,400,0.3,(0,255,0)),Cubo(100,650,250,0.5,(0,0,255)),Cubo(100,600,50,0.1,(255,255,0)),Cubo(87,650,150,0.2,(139,69,19))]
textos=[Texto("testando menu",(210,0,0),810,50,20,True),Texto('teste 2',(0,210,0),810,100,20,True)]

main=Main(1000,600,textos,cubos)

main.rodar()



pygame.quit()
