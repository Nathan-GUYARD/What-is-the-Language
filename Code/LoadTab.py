"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente l'affichege de tout les élements de l'arbre en liste

--------------------------------------------------------------------"""
from Button import*
from screenPygame import*

class LoadTab:
    """
    Rôle    : Affichage d'un tableau
    """
    
    def __init__(self,tab):
        """
        Rôle    : Initialise l'affichage des mots
        Entré   : le tableau contenant tout les mots (list)
        Sortie  : Rien
        """

        # booléen de l'état de la fenetre
        self.endTab = False
        
        # crée un boutton
        self.selParcours = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/selParcours.png")

        self.tabWord = tab
        # idice de la liste, du premier mot afficher
        self.parcourValue = 0

        # crée le texte qui affiche le nombre de mots
        self.nbWord = FONT_NAME.render("Il y a {} mots".format(str(len(self.tabWord))),True,WHITE)
        self.loadWords()
        

    def loadWords(self):
        """
        Rôle    : Affiche les mots
        Entré   : Rien
        Sortie  : Rien
        """

        tabWord = []
        xtab = 0
        ytab = 0
        # recupère les mots 1 par 1, 20 à la fois
        for word in self.tabWord[self.parcourValue:self.parcourValue+20]:
            
            # crée le texte du mot
            loadWord = FONT_NAME.render(word,True,WHITE)
            # ajoute a la liste des mots qui vont être affiché
            tabWord.append(loadWord)

            # ajoute a largeur du mots
            ytab += loadWord.get_height() + 5

            # recherche le mots avec la longueur la plus grande
            if loadWord.get_width() > xtab:
                xtab = loadWord.get_width()
        
        # crée une surface intermediaire vide 
        self.opacitySurf = pygame.Surface((xtab,ytab),pygame.SRCALPHA)
        self.opacitySurf.fill((255,255,255,0))
        
        y = 0
        # pour chaque mot le placer sur la surface intermédiaire
        for word in tabWord:
            self.opacitySurf.blit(word,(0,y))
            y += word.get_height() + 5
        
        # crée un fond
        self.backround = pygame.Surface((self.opacitySurf.get_width()+50,SIZE_SCREEN[1]-300))
        self.backround.fill(GREY)

        
    def load(self):
        """
        Rôle    : Affiche la fenetre
        Entré   : Rien
        Sortie  : Rien
        """

        # vérifi si la fenetre n'est pas quitté
        if not self.endTab:
            # affiche un fond noir
            SCREEN.fill(BLACK)

            # affiche le mot
            self.backround.blit(self.opacitySurf,(10,15))
            SCREEN.blit(self.backround,(25,25))

            # affiche le boutton
            self.selParcours.load()

            # affiche le nombre de mots
            SCREEN.blit(self.nbWord,(SIZE_SCREEN[0]-self.nbWord.get_width()-5,5))


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

                # verifi si le boutton est cliqué
                if self.selParcours.isClic(pos):
                    self.endTab = True


    def isScrolling(self,event):
        """
        Rôle    : Vérifie la mollete est utilisé et dessant ou augmente la position dans la liste de mots
        Entré   : Rien
        Sortie  : Rien
        """
        
         # verifi si le scrol de la souris est utilisé
        if event.type == pygame.MOUSEWHEEL:
            # augmente ou diminue l'indice du premier mot qui va être affiché
            self.parcourValue += event.y * -10
            min = 0
            max = len(self.tabWord) - 10

            # vérifi si la valeur est supérieur a 0
            if self.parcourValue < min:
                self.parcourValue = min

            # vérifi si la valeur est inférieur au nombre de mot - 10
            elif self.parcourValue > max:
                self.parcourValue = max
            
            # met a jour l'affichage des mots
            self.loadWords()


#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = LoadTab(["test"])
    
    while True:
        
        test.load()

        event = pygame.event.poll()
        
        test.buttonsIsClic(event)

        
        test.isScrolling(event)
        
        pygame.display.flip()

        if event.type == pygame.QUIT :
            # met fin a la boucle principale
            end = False
            # ferme la fenetre
            quit()

