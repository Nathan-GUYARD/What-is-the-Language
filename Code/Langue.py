"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente une langue

--------------------------------------------------------------------"""
from Dico import*

class Language:
    """
    Role    : Crée une langue
    """
    
    def __init__(self,name):
        """
        Rôle    : Initialise la langue
        Entré   : Le nom de la langue (str)
        Sortie  : Rien
        """

        self.name = name
        # crée le dictionnaire de la langue
        self.dico = Dico("Dico/"+self.name+".txt")

    def __repr__(self):
        """
        Rôle    : Defini la representation de la langue
        Entré   : Rien
        Sortie  : Le nom de la langue (str)
        """
    
        return self.name

    def wordIsInLanguage(self,word):
        """
        Rôle    : Recherche si le mot est dans la langue
        Entré   : le mot recherché (str)
        Sortie  : si le mot est dans le dictionnaire (bool)
        """
        
        return self.dico.abr.isInABR(word)


