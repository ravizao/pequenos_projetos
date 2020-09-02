import pygame
from pygame.locals import *
import math



class Vertice:
    def __init__(self,x,y,z):
        self.z=z
        self.x=x/z
        self.y=y/z

class Aresta:
    def __init__(self,tamanho,grossura,inicio,fim):
        self.tamanho=tamanho
        self.inicio=inicio
        self.fim=fim

        self.rect_orig=pygame.Surface((grossura,tamanho))
        self.rect_orig.set_colorkey((0,0,0))
        self.rect_orig.fill((0,255,0))

        self.imagen=self.rect_orig.copy()
        self.imagen.set_colorkey((0,0,0))
        self.rect=self.imagen.get_rect()
        self.rect.center=((inicio[0]+fim[0])/2,(inicio[1]+fim[1])/2)

    def angulo(self,a,b):

        dotProduct = a[0]*b[0] + a[1]*b[1]
        modOfVector1 = math.sqrt( a[0]*a[0] + a[1]*a[1])*math.sqrt(b[0]*b[0] + b[1]*b[1])
        angle = dotProduct/modOfVector1
        return math.degrees(math.acos(angle))





    def rodar(self,tela):
        old_center = self.rect.center

        rot = self.angulo(self.inicio,self.fim)
        # rotating the orignal image
        print(rot)
        nova_imagen = pygame.transform.rotate(self.rect_orig , -90+2*rot)
        rect = nova_imagen.get_rect()
        # set the rotated rectangle to the old center
        rect.center = old_center
        # drawing the rotated rectangle to the screen
        tela.blit(nova_imagen , rect)
        pygame.draw.rect(tela,(0,255,0),(self.inicio[0],self.inicio[1],10,10))
        pygame.draw.rect(tela,(0,255,0),(self.inicio[0],self.inicio[1],10,10))


class Triangulo:
    def __init__(self,v1,v2,v3,a1,a2,a3):
        self.vertices=[v1,v2,v3]
        self.arestas=[a1,a2,a3]








def main():
    tela = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    done = False
    aresta=Aresta(50,2,(100,200),(400,150))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        aresta.rodar(tela)


        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
