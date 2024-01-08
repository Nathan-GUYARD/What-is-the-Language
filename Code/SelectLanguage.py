"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente la selection de la langue

--------------------------------------------------------------------"""
from SelectParcours import*

class SelectLanguages:
    """
    Rôle    : Selection de la langue
    """
    
    def __init__(self):
        """
        Rôle    : Initialise la selection de la langue
        Entré   : Rien
        Sortie  : Rien
        """
        
        # booléens de l'état de la fenetre
        self.endSelectLanguage = False
        self.inSelectParcours = False

        # crée un boutton pour retourné au menu
        self.menu = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/menu.png")
        
        # récupère la liste de toutes les langues
        allLanguages = list(LANGUAGE_ABR.keys())
        
        self.languages = []

        y = 100
        
        # répète 2 fois
        for i in range (6):
            # si i est divisible par 3
            if i%3 == 0:
                # gauche de l'écran
                x = 100

            # si le reste de la division euclidiènne par 3 est 1
            elif i%3 == 1:
                # milieu de l'écran
                x = (SIZE_SCREEN[0]-300)//2

            # si le reste de la division euclidiènne par 3 est 1
            else:
                # droite de l'écran
                x = SIZE_SCREEN[0]-400
            
            # crée un boutton pour chaque langue
            self.languages.append(Button(x,y,300,200,"image/{}.png".format(allLanguages[i])))
            
            if i == 2:
                # baisse la hauteur les prochains bouttons
                y += 250
                
            
    def select(self,nb):
        """
        Rôle    : selectionne la langue
        Entré   : numero de la langue (int)
        Sortie  : nom de la langue (str)
        """
        
        # envoie une erreur si le nombre est plus petit que 0 ou supérieur à 6
        assert nb >= 0 or nb < 6

        return LANGUAGE_ABR[list(LANGUAGE_ABR.keys())[nb]]


    def load(self):
        """
        Rôle    : Ajoute des manches
        Entré   : Nombre de manche en plus (int)
        Sortie  : Rien
        """

        if not self.endSelectLanguage and not self.inSelectParcours:
            # affiche un fond noir
            SCREEN.fill(BLACK)
            
            # affiche les bouttons
            for button in self.languages:
                button.load()
            self.menu.load()

        # si l'utilisateurs sélectionne le type de parcours
        elif self.inSelectParcours:
            self.selParcours.load()

    def buttonsIsClic(self,event):
        """
        Rôle    : Verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """
        
        # si l'utilisateurs sélectionne le type de parcours
        if self.inSelectParcours:
            self.selParcours.buttonsIsClic(event)
            # si la selction du parcours est fini
            if self.selParcours.endSelParcours:
                self.inSelectParcours = False

        # si un boutton de la souris est cliqué
        elif event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and event.button != pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()
                
                # vérifi si les boutton sont cliqués
                if self.menu.isClic(pos):
                    self.endSelectLanguage = True

                # pour chaque langue
                for i in range (len(self.languages)):
                    if self.languages[i].isClic(pos):
                        # lance la sélection du parcours en fonction de la langue selectionné
                        self.selParcours = SelectParcours(self.select(i))
                        self.inSelectParcours = True


#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------     

if __name__ == '__main__':

    test = SelectLanguages()

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