"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente la selection du type d'affichage de l'arbre

--------------------------------------------------------------------"""
from LoadABR import*
from LoadTab import*

class SelectParcours:
    """
    Rôle    : Selection du type de parcours
    """

    def __init__(self,language):
        """
        Rôle    : Initialise la selection du type de parcours
        Entré   : nom de la langue (str)
        Sortie  : Rien
        """

        # booléens de l'état de la fenetre
        self.inArbre = False
        self.inParcours = False
        self.endSelParcours = False

        self.language = str(language)
        # crée un boutton pour retourné à la sélection de la langue
        self.selLang = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/selLanguage.png")

        nameParcours = ["prefixe","infixe","suffixe","largeur","arbre"]
        
        self.parcours = []
        # répète 5 fois
        for i in range (5):
            # si i est plus petit que 2
            if i <= 2:
                y = 100
                
                if i%3 == 0:
                    # gauche de l'écran
                    x = 100
                elif i%3 == 1:
                    # milieu de l'écran
                    x = (SIZE_SCREEN[0]-300)//2
                else:
                    # droite de l'écran
                    x = SIZE_SCREEN[0]-400
                    
            else:
                y = 350
                if i%3 == 0:
                    # gauche de l'écran
                    x = 300
                else:
                    # droite de l'écran
                    x = SIZE_SCREEN[0]-600
            
            # crée le boutton
            self.parcours.append(Button(x,y,300,200,"image/{}.png".format(nameParcours[i])))
    

    def load(self):
        """
        Rôle    : Ajoute des manches
        Entré   : Nombre de manche en plus (int)
        Sortie  : Rien
        """

        # si le parcours choisi est l'arbre
        if self.inArbre:
            self.arbre.load()
        
        # si le parcours choisi est dans le format d'un tableau
        elif self.inParcours:
            self.loadWords.load()

        elif not self.endSelParcours:
            # affiche un fond noir
            SCREEN.fill(BLACK)

            # affiche les bouttons
            self.selLang.load()
            for button in self.parcours:
                button.load()


    def buttonsIsClic(self,event):
        """
        Rôle    : Verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """

        # si le parcours choisi est dans le format d'un tableau
        if self.inParcours:
            self.loadWords.isScrolling(event)
            self.loadWords.buttonsIsClic(event)

            # si l'affichage de l'arbre est fini
            if self.loadWords.endTab:
                self.inParcours = False

        # si le parcours choisi est l'arbre    
        elif self.inArbre:
            self.arbre.buttonsIsClic(event)
            # si l'affichage de l'arbre est fini
            if self.arbre.endArbre:
                self.inArbre = False

        # si un boutton de la souris est cliqué
        elif event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and event.button != pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()
                
                # vérifi si le boutton sont cliqués
                if self.selLang.isClic(pos):
                    self.endSelParcours = True

                # pour chaque boutton
                for i in range (len(self.parcours)):
                    # vérifi si le boutton est cliqués
                    if self.parcours[i].isClic(pos):

                        # si c'est un parcours infixe,suffixe,...
                        if i <= 3:
                            if i == 0:
                                # récupère le tableau du parcours préfixe sur l'arbre
                                tabWord = LANGUAGE_ABR[self.language].dico.abr.parcourPre()
                                
                            elif i == 1:
                                # récupère le tableau du parcours infixe sur l'arbre
                                tabWord = LANGUAGE_ABR[self.language].dico.abr.parcourInf()
                                
                            elif i == 2:
                                # récupère le tableau du parcours suffixe sur l'arbre
                                tabWord = LANGUAGE_ABR[self.language].dico.abr.parcourSuf()
                                
                            else:
                                # récupère le tableau du parcours en largeyr sur l'arbre
                                tabWord = LANGUAGE_ABR[self.language].dico.abr.parcourLarg()

                            # lance l'affichage de l'arbre au format d'un tableau
                            self.loadWords = LoadTab(tabWord)
                            self.inParcours = True
                            
                        else:
                            # lance l'affichage de l'arbre
                            self.arbre = LoadABR(LANGUAGE_ABR[self.language].dico.abr)
                            self.inArbre = True


        
#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':

    test = SelectParcours("francais")

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