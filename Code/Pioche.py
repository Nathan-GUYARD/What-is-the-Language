"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente la pioche,stock tous les mots 
            qui peuvent etre choisi au hasard

--------------------------------------------------------------------"""
import random

class Pool:
    """
    Rôle    : Crée la pioche
    """
    
    def __init__(self,tablanguage):
        """
        Rôle    : Initialise la pioche
        Entré   : tout les languages dans la pioche (list)
        Sortie  : Rien
        """
    
        self.tabword = []
        # récupère tout les mots
        for language in tablanguage:
            # ouvre le fichier d'un dictionnaire
            with open("Dico/"+language+".txt","r",encoding="UTF-8") as file:
                self.tabword += file.read().split("\n")

    def chooseWord(self):
        """
        Rôle    :   Choisi le mot au hazar
        Entré   : Rien
        Sortie  : le mot choisi (str)
        """

        # retourn un mot au hasard
        return self.tabword[random.randint(0,len(self.tabword))]
    
    





