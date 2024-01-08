"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente l'affichege de l'arbre

--------------------------------------------------------------------"""
from Button import*
from screenPygame import*
from languageABR import*
from pile import*

class LoadABR:
    """
    Role    : Affichage d'un ABR
    """
    
    def __init__(self,abr):
        """
        Rôle    : Initialise l'affichage de l'ABR
        Entré   : l'ABR (ABR)
        Sortie  : Rien
        """

        # booléen de la fin de l'affichage de l'arbre
        self.endArbre = False
        
        # crée une pile
        self.pile = Pile()

        # stock la racine de l'arbre
        self.elem = abr
        # crée le texte du mot
        self.word = FONT.render(self.elem.value,True,WHITE)
        # crée le fond du mot
        self.backroundWord = pygame.Surface((self.word.get_width()+100,50))
        self.backroundWord.fill(GREY)
        self.backroundWord.blit(self.word,((self.backroundWord.get_width() - self.word.get_width())//2, 5))

        # crée les bouttons
        self.selParcours = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/selParcours.png")
        self.left = Button(100,350,300,200,"image/left.png")
        self.right = Button(SIZE_SCREEN[0]-400,350,300,200,"image/right.png")
        self.back = Button((SIZE_SCREEN[0]-300)//2,350,300,200,"image/back.png")

        # crée le texte du nombre de mots et de la hauteur de l'arbre
        self.nbWord = FONT_NAME.render("Il y a {} mots".format(str(len(self.elem))),True,WHITE)
        self.hauteur = FONT_NAME.render("hauteur de l'arbre : {}".format(str(self.elem.height())),True,WHITE)

    def goLeft(self):
        """
        Rôle    : Va a gauche du noeud
        Entré   : Rien
        Sortie  : Rien
        """

        # ajoute l'element dans la pile
        self.pile.pushElem(self.elem)

        # le nouvel element devient l'arbre gauche de l'ancien
        self.elem = self.elem.left
        self.word = FONT.render(self.elem.value,True,WHITE)

        # crée le fond du mot
        self.backroundWord = pygame.Surface((self.word.get_width()+100,50))
        self.backroundWord.fill(GREY)
        self.backroundWord.blit(self.word,((self.backroundWord.get_width() - self.word.get_width())//2, 5))

    def goRight(self):
        """
        Rôle    : Va a droite du noeud
        Entré   : Rien
        Sortie  : Rien
        """

        # ajoute l'element dans la pile
        self.pile.pushElem(self.elem)

        # le nouvel element devient l'arbre gauche de l'ancien
        self.elem = self.elem.right
        # crée le texte du mot
        self.word = FONT.render(self.elem.value,True,WHITE)

        # crée le fond du mot
        self.backroundWord = pygame.Surface((self.word.get_width()+100,50))
        self.backroundWord.fill(GREY)
        self.backroundWord.blit(self.word,((self.backroundWord.get_width() - self.word.get_width())//2, 5))
    def goBack(self):
        """
        Rôle    : retourne en arrière dans l'arbre
        Entré   : Rien
        Sortie  : Rien
        """

        # enleve le dernier element de la pile
        self.elem = self.pile.popElem()
        # crée le texte du mot
        self.word = FONT.render(self.elem.value,True,WHITE)

        # crée le fond du mot
        self.backroundWord = pygame.Surface((self.word.get_width()+100,50))
        self.backroundWord.fill(GREY)
        self.backroundWord.blit(self.word,((self.backroundWord.get_width() - self.word.get_width())//2, 5))

    def load(self):
        """
        Rôle    : Affiche l'arbre
        Entré   : Rien
        Sortie  : Rien
        """

        # si l'affichage de l'arbe n'est pas fini
        if not self.endArbre:
            # affiche un fond noir
            SCREEN.fill(BLACK)

            # affiche le mot
            SCREEN.blit(self.backroundWord,((SIZE_SCREEN[0]-self.backroundWord.get_width())//2, 100))

            # affiche le boutton por retourner à la selection du parcours
            self.selParcours.load()

            # si l'arbre guache existe
            if self.elem.left != None:
                # affiche le boutton pour aller à gauche
                self.left.load()
            
            # si l'arbre droite existe
            if self.elem.right != None:
                # affiche le boutton pour aller à droite
                self.right.load()
            
            # si la pile est vide
            if not self.pile.isEmpty():
                # affiche le boutton pour aller en arrière
                self.back.load()

            # affiche le nombre de mots et la hauteur de l'arbre
            SCREEN.blit(self.nbWord,(SIZE_SCREEN[0]-self.nbWord.get_width()-5,5))
            SCREEN.blit(self.hauteur,(SIZE_SCREEN[0]-self.hauteur.get_width()-5,10 + self.nbWord.get_height()))


    def buttonsIsClic(self,event):
        """
        Rôle    : verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """
        
        # si un boutton de la souris est cliqué
        if event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()

                # verifi si les bouttons sont cliqués
                if self.selParcours.isClic(pos):
                    self.endArbre = True
                    
                elif self.left.isClic(pos) and self.elem.left != None:
                    # va a gauche
                    self.goLeft()

                elif self.right.isClic(pos) and self.elem.right != None:
                    # va a droite
                    self.goRight()

                elif self.back.isClic(pos) and not self.pile.isEmpty():
                    # va en arrière
                    self.goBack()


#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = LoadABR(LANGUAGE_ABR["francais"].dico.abr)
    
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
