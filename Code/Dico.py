"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente le dictionnaire

--------------------------------------------------------------------"""
from ABR import *
import random

class Dico:
    """
    Role    : Crée un dictionnaire
    """
    
    def __init__(self,folder):
        """
        Rôle    : Initialise le dictionnaire
        Entré   : Le chemin du fichier contenant les mots (str)
        Sortie  : Rien
        """

        # ouvre le fichier et recupère les mots dans une liste
        with open(folder,"r",encoding="UTF-8") as file:
            tabword = file.read().split("\n")

        # crée un ABR
        self.abr = ABR(tabword.pop(random.randint(0,len(tabword)-1)))

        # range tous les mots dans l'ABR un par un au hasard
        while len(tabword)>0:
            self.abr.insert(tabword.pop(random.randint(0,len(tabword)-1)))
            
            



#------------------------------------------------------------------------------------------
# TEST
#------------------------------------------------------------------------------------------

if __name__ == '__main__':
    Dico("test.txt")



