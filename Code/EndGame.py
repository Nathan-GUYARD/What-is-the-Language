"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente l'affichege a la fin de la partie

--------------------------------------------------------------------"""
from Button import *

class EndGame:
    """
    Role    : Affiche le resultat de la manche et passe à la prochaine manche
    """
    
    def __init__(self,score):
        """
        Rôle    : Initialise le menu pour continuer la partie
        Entré   : victoire (bool)
        Sortie  : Rien
        """

        # crée le texte qui affiche le résultat de la partie
        self.score = FONT.render("Bien joué vous avez {} {}".format(str(score),"point" if score <= 1 else "points"),True,WHITE)
        # crée le fond du texte
        self.backround = pygame.Surface((self.score.get_width()+50,50))
        self.backround.fill(GREY)
        self.backround.blit(self.score,(25,5))

        # crée un boutton pour rejouer
        self.continu = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/replay.png")

        # boolean de l'état de la fenetre
        self.stopEndGame = False


    def load(self):
        """
        Rôle    : Affiche le menu
        Entré   : Rien
        Sortie  : Rien
        """

        # tant que la fenetre n'est pas quitté 
        if not self.stopEndGame:
            
            # affiche un fond noir
            SCREEN.fill(BLACK)

            # affiche le boutton
            self.continu.load()
            # affiche le texte
            SCREEN.blit(self.backround,((SIZE_SCREEN[0]-self.backround.get_width())//2, 200))


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

                # verifi si le boutton pour rejouer est cliqué
                if self.continu.isClic(pos):
                    self.stopEndGame = True



#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = EndGame(0)

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