"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente le menu principale du jeu

--------------------------------------------------------------------"""
from SelectLanguage import*
from Partie import*

class Menu:
    """
    Role    : Crée la Menu
    """
    def __init__(self):
        """
        Rôle    : Initialise le Menu
        Entré   : Rien
        Sortie  : Rien
        """
        
        # booléens de l'état de la fenetre
        self.inDico = False
        self.inGame = False

        # crée les bouttons
        self.play = Button((SIZE_SCREEN[0]-400)//2,(SIZE_SCREEN[1]-300)//2-150,400,300,"image/play.png")
        self.dico = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/dico.png")


    def load(self):
        """
        Rôle    : Affiche la fenetre
        Entré   : Rien
        Sortie  : Rien
        """
        
        if self.inDico:
            # affiche la selection de la langue
            self.SelLanguage.load()


        elif self.inGame:
            # affiche la selection de la partie
            self.game.load()

        else:
            # affiche un fond noir
            SCREEN.fill(BLACK)
            
            # affiche les boutons
            self.play.load()
            self.dico.load()


    def buttonsIsClic(self,event):
        """
        Rôle    : verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """

        if self.inGame:
            # vérifi si les bouttons de la partie sont cliqués
            self.game.buttonsIsClic(event)
            # si la partie est fini
            if self.game.endPartieSelect and not self.game.inManche:
                self.inGame = False

        elif self.inDico:
            # vérifi si les bouttons de la selection de la langue sont cliqués
            self.SelLanguage.buttonsIsClic(event)
            # si la selection de la langue est quitté
            if self.SelLanguage.endSelectLanguage:
                self.inDico = False

        # si un boutton de la souris est cliqué
        elif event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and event.button != pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()

                # vérifi si les boutton sont cliqués
                if self.play.isClic(pos):
                    # lance le choix de la partie
                    self.game = Partie()
                    self.inGame = True

                if self.dico.isClic(pos):
                    # lance la selection de la langue
                    self.SelLanguage = SelectLanguages()
                    self.inDico = True


#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = Menu()

    while True:
        SCREEN.fill(BLACK)
        test.load()

        event = pygame.event.poll()

        test.buttonsIsClic(event)
        
        pygame.display.flip()

        if event.type == pygame.QUIT :
            # met fin a la boucle principale
            end = False
            # ferme la fenetre
            quit()