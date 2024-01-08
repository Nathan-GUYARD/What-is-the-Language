"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente la gestion d'une manche

--------------------------------------------------------------------"""
from Pioche import *
from languageABR import *
from Continue import *
from Player import*


class Manche:
    """
    Role    : Crée une Manche
    """
    
    def __init__(self,languagepossibility,player):
        """
        Rôle    : Initialise la manche
        Entré   : les languages possible (list)
        Sortie  : Rien
        """

        self.player = player
        # crée le texte du score
        self.score = FONT.render("{} point{}".format(str(self.player.score),"s"if self.player.score>1 else ""),True,WHITE)

        # booléens de l'état de la partie
        self.endManche = False
        self.inContinu = False
        self.exitToPartie = False

        # choisi un mot
        self.word = Pool(languagepossibility).chooseWord()

        # copie la liste des languages
        language = []
        language += languagepossibility

        self.languages = []
        # effectue 2 fois
        for i in range (2):
            # ajoute une langue au hasard et évite d'avoir 2 fois le même
            self.languages.append(language.pop(random.randint(0,len(language)-1)))
        self.languages.append("other")

        # crée le boutton por retourner dans la sélection de la partie
        self.replay = Button((SIZE_SCREEN[0]-300)//2,SIZE_SCREEN[1]-250,300,200,"image/replay.png")
        # crée les bouttons pour choisir la langue
        self.language1 = Button(100,300,300,200,"image/"+self.languages[0]+".png")
        self.language2 = Button((SIZE_SCREEN[0]-300)//2,300,300,200,"image/"+self.languages[1]+".png")
        self.other = Button(SIZE_SCREEN[0]-400,300,300,200,"image/other.png")

        # crée le mot
        self.wordTitle = FONT_NAME.render("Le mot est :",True,WHITE)
        self.wordtxt = FONT.render(self.word,True,WHITE)
        # crée un fond pour le mot
        self.backroundWord = pygame.Surface((500,60))
        self.backroundWord.fill(GREY)
        # ajoute le mot sur le fond
        self.backroundWord.blit(self.wordtxt,((self.backroundWord.get_width()-self.wordtxt.get_width())//2, 10))
        

    def selectLanguage(self,languageselect):
        """
        Rôle    : Vérifie si le langage choisi est le bon 
        Entré   : le langage selectionné (str)
        Sortie  : Rien
        """

        # si le joueur a choisi une langue en particulier
        if languageselect != "other":
            # vérifi la parmière langue
            if LANGUAGE_ABR[languageselect].wordIsInLanguage(self.word) == True:
                self.win = True
                self.player.score += 1

            # vérifi la deuxième langue 
            else:
                self.win = False
        
        # vérifi si le mot est dans la parmière langue ou dans la deuxième langue alors que le jour a choisi autre
        elif LANGUAGE_ABR[self.languages[0]].wordIsInLanguage(self.word) or LANGUAGE_ABR[self.languages[1]].wordIsInLanguage(self.word):
            self.win = False
        
        # si la repouse autre est la bonne réponse
        else:
            self.win = True
            self.player.score += 1
        

    def load(self):
        """
        Rôle    : Affiche la fenetre
        Entré   : Rien
        Sortie  : Rien
        """

        # si la manche n'est pas partie
        if not(self.exitToPartie):
            # si la manche n'est pas fini
            if not(self.endManche) :
                # affiche un fond noir
                SCREEN.fill(BLACK)

                # affiche les bouttons
                self.replay.load()
                self.language1.load()
                self.language2.load()
                self.other.load()
                
                # affiche les textes
                SCREEN.blit(self.wordTitle,((SIZE_SCREEN[0]-self.wordTitle.get_width())//2,50))
                SCREEN.blit(self.backroundWord,((SIZE_SCREEN[0]-self.backroundWord.get_width())//2,150))
                SCREEN.blit(self.score,(SIZE_SCREEN[0]-self.score.get_width()-5,5))

            # si la manche
            elif self.inContinu:
                # affiche la fenetre apres la fin de la manche
                self.continu.load()
                
                # si le joueur continu
                if self.continu.endContinu:
                    self.inContinu = False


    def buttonsIsClic(self,event):
        """
        Rôle    : verifi si les bouttons sont cliqués
        Entré   : Les events de la page (pygame.event)
        Sortie  : Rien
        """

        # si la manche est fini
        if self.inContinu:
            self.continu.buttonsIsClic(event)

        # si un boutton de la souris est cliqué
        elif event.type == pygame.MOUSEBUTTONUP:
            # verifi si le boutton cliqué n'est pas le scrol de la souris
            if event.button != pygame.BUTTON_WHEELDOWN and event.button != pygame.BUTTON_WHEELUP:
                # recupère la position de la souris
                pos = pygame.mouse.get_pos()

                # si la partie ou la manche n'est pas fini
                if not self.exitToPartie and not self.endManche:
                    
                    # vérifi si les boutton sont cliqués
                    if self.replay.isClic(pos):
                        self.exitToPartie = True

                    elif self.language1.isClic(pos):
                        # vérifi si c'est la bonne réponse
                        self.selectLanguage(self.languages[0])
                        
                        # fin de la manche
                        self.endManche = True
                        self.inContinu = True
                        self.continu = Continue(self.win)

                    elif self.language2.isClic(pos):
                        # vérifi si c'est la bonne réponse
                        self.selectLanguage(self.languages[1])

                        # fin de la manche
                        self.endManche = True
                        self.inContinu = True
                        self.continu = Continue(self.win)
                        
                    elif self.other.isClic(pos):
                        # vérifi si c'est la bonne réponse
                        self.selectLanguage(self.languages[2])
                        
                        # fin de la manche
                        self.endManche = True
                        self.inContinu = True
                        self.continu = Continue(self.win)

        


#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':
    test = Manche(["francais","allemand","anglais","espagnol","italien","neerlandais"],Player())

    while True:
        
        event = pygame.event.poll()
        
        test.buttonsIsClic(event)
            
        test.load()


        pygame.display.flip()

        if event.type == pygame.QUIT :
            # met fin a la boucle principale
            end = False
            # ferme la fenetre
            quit()


