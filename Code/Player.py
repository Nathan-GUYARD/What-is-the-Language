"""--------------------------------------------------------------------

Auteur  :    Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente la class joueur

--------------------------------------------------------------------"""
class Player:
    """
    Rôle    : crée le jour et gère son nombre de point
    """
    
    def __init__(self):
        """
        Rôle    : Initialise le joueur
        Entré   : Rien
        Sortie  : Rien
        """
        # crée le score
        self.score = 0