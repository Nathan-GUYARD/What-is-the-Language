"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   crée la fenetre pygame et les couleurs et les fonts

--------------------------------------------------------------------"""
import pygame

# crée la fenetre
pygame.init()
pygame.display.set_caption("What Is The Language")
SIZE_SCREEN = [1250,920]
SCREEN = pygame.display.set_mode((SIZE_SCREEN[0], SIZE_SCREEN[1]))

# crée les font
pygame.font.init()
FONT_NAME = pygame.font.Font(pygame.font.get_default_font(), 30)
FONT = pygame.font.Font(pygame.font.get_default_font(), 40)


# crée les couleurs
GREY = (30,30,30)
WHITE = (255,255,255)
BLACK = (0,0,0)

# affiche le mot chargement sur la fenetre
loading = FONT.render("Chargement...",True,WHITE)
SCREEN.blit(loading,((SIZE_SCREEN[0]-loading.get_width())//2,(SIZE_SCREEN[1]-loading.get_height())//2))
pygame.display.flip()