"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente le choix des parametres de la partie

--------------------------------------------------------------------"""
from Manche import *
from EndGame import *

class Partie:
    """
    Role    : Crée la partie
    """
    
    def __init__(self) :
        """
        Rôle    : Initialise la partie
        Entré   : Rien
        Sortie  : Rien
        """
        
        # crée un joueur
        self.player = Player()

        # initialise le nombre de manche par défaut
        self.nbmanche = 5
        # récupère toutes les langues
        self.languages = list(LANGUAGE_ABR.keys())

        # booléens de l'état de la fenetre
        self.inEndGame = False
        self.inManche = False
        self.endPartieSelect = False

        # crée les bouttons
        self.menu = Button(SIZE_SCREEN[0]//2-150,SIZE_SCREEN[1]-300,300,200,"image/menu.png")
        self.moremanche = Button(100,500,80,80,"image/more.png")
        self.lessmanche = Button(250,500,80,80,"image/less.png")
        self.play = Button((SIZE_SCREEN[0]-400)//2,(SIZE_SCREEN[1]-300)//2-150,400,300,"image/play.png")

        # crée les textes du nombre de manche
        self.nbmanchetxt = FONT.render(str(self.nbmanche),True,WHITE)
        self.loadNbManche = FONT_NAME.render("Nombre de manche :",True,WHITE)
        

    def startManche(self):
        """
        Rôle    : Commence la manche
        Entré   : Rien
        Sortie  : Rien
        """

        # modifi les booléens de la manche
        self.inManche = True
        self.endPartieSelect = True

        # crée une manche
        self.currentmanche = Manche(self.languages,self.player)


    def newManche(self):
        """
        Rôle    : Commence une nouvelle manche
        Entré   : Rien
        Sortie  : Rien
        """
        
        # si il reste des manches
        if self.nbmanche > 0:
            self.nbmanche += -1
            
            # commence une manche
            self.startManche()

        # si il n'y a plus de manche
        else :
            # met fin a la partie
            self.inManche = False
            self.endPartieSelect = False
            self.inEndGame = True

            # crée le menu qui affiche le résultat
            self.endGame = EndGame(self.player.score)

            # modifi les valeurs de score et de manche
            self.nbmanche = 5
            self.nbmanchetxt = FONT.render(str(self.nbmanche),True,WHITE)
            self.player.score = 0
            

    def load(self):
        """
        Rôle    : Affiche la fenetre
        Entré   : Rien
        Sortie  : Rien
        """
            
        # si la partie est fini
        if self.inEndGame:
            self.endGame.load()

        # si la partie n'a pas encore commencé
        elif not self.endPartieSelect:
            # affiche un fond noir
            SCREEN.fill(BLACK)

            # affiche les boutons
            self.menu.load()
            self.moremanche.load()
            self.lessmanche.load()
            self.play.load()

            # affiche le nombre de manche
            backroundNbManche = pygame.Surface((50,45))
            backroundNbManche.fill(GREY)
            backroundNbManche.blit(self.nbmanchetxt,((backroundNbManche.get_width()-self.nbmanchetxt.get_width())//2, (backroundNbManche.get_height()-self.nbmanchetxt.get_height())//2))
            SCREEN.blit(backroundNbManche,(190,430))
            SCREEN.blit(self.loadNbManche,(75,380))

        # si la manche est commencé
        elif self.inManche:
            # affiche la manche
            self.currentmanche.load()

            # si la manche est fini commencé une nouvelle manche
            if self.currentmanche.endManche and not self.currentmanche.inContinu:
                self.newManche()

            # si le jour retourne a la selection de la partie
            if self.currentmanche.exitToPartie:
                # met fin a la partie
                self.inManche = False
                self.currentmanche.endManche = True
                self.endPartieSelect = False

                # modifi les valeurs de score et de manche
                self.nbmanche = 5
                self.nbmanchetxt = FONT.render(str(self.nbmanche),True,WHITE)
                self.player.score = 0
            

    def changeNomberManche(self,nb):
        """
        Rôle    : Ajoute des manches
        Entré   : Nombre de manche en plus (int)
        Sortie  : Rien
        """

        # si le nombre de manche peux etre encore diminué ou augmenté
        if (nb > 0 or (self.nbmanche > 1 and nb < 0)) and (nb < 0 or (self.nbmanche < 99 and nb > 0)):
            # change le nombre de manche
            self.nbmanche += nb
            self.nbmanchetxt = FONT.render(str(self.nbmanche),True,WHITE)


    def buttonsIsClic(self,event):
        """
        Rôle    : Verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """

        # si la manche est commencé
        if self.inManche:
            # vérifi si les bouttons de la manche sont cliqués
            self.currentmanche.buttonsIsClic(event)

        # si la partie est fini
        elif self.inEndGame:
            # vérifi si les bouttons du résultat sont cliqués
            self.endGame.buttonsIsClic(event)

            # si le résultat est fini
            if self.endGame.stopEndGame:
                self.inEndGame = False

        # si un boutton de la souris est cliqué
        elif event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and event.button != pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()

                # vérifi si les boutton sont cliqués
                if self.menu.isClic(pos):
                    self.endPartieSelect = True

                if self.play.isClic(pos):
                    # lance la partie
                    self.newManche()

                if self.moremanche.isClic(pos):
                    # ajoute 1 manche
                    self.changeNomberManche(1)

                if self.lessmanche.isClic(pos):
                    # retire 1 manche
                    self.changeNomberManche(-1)

            


#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = Partie()

    inPartie = True
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



