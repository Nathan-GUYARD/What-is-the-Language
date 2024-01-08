"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente l'affichage à la fin d'une manche

--------------------------------------------------------------------"""
from Button import *

class Continue:
    """
    Role    : Affiche le resultat de la manche et passe à la prochaine manche
    """
    
    def __init__(self,win):
        """
        Rôle    : Initialise le menu pour continuer la partie
        Entré   : victoire (bool)
        Sortie  : Rien
        """

        # le texte qui affiche le resultat de la manche
        win = FONT.render("Vous avez {} !".format("gagné"if win else "perdu") ,True,WHITE)
        
        # crée le fond du texte
        self.backroundWin = pygame.Surface((400,50))
        self.backroundWin.fill(GREY)
        # ajoute le texte sur le fond
        self.backroundWin.blit(win,((self.backroundWin.get_width() - win.get_width())//2, 5))

        # crée un boutton pour continuer la partie
        self.continu = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/continu.png")

        # crée le booléen de l'état de l'affichage 
        self.endContinu = False


    def load(self):
        """
        Rôle    : Affiche le menu
        Entré   : Rien
        Sortie  : Rien
        """

        # si la manche suivante n'est pas commencé
        if not self.endContinu:
            
            # affiche un fond noir
            SCREEN.fill(BLACK)

            # affiche le boutton
            self.continu.load()
            # affiche le texte
            SCREEN.blit(self.backroundWin,((SIZE_SCREEN[0]-self.backroundWin.get_width())//2, 200))


    def buttonsIsClic(self,event):
        """
        Rôle    : verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """

        # si un boutton de la souris est cliqué
        if event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and event.button != pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()

                # verifi si le boutton pour continuer est cliqué
                if self.continu.isClic(pos):
                    self.endContinu = True



#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = Continue(True)

    while True:
        test.load()
        
        event = pygame.event.poll()
        
        test.buttonsIsClic(event)

        pygame.display.flip()

        if event.type == pygame.QUIT :
            # met fin a la boucle principale
            end = False
            # ferme la fenetre
            quit()