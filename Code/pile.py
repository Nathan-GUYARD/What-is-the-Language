"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente une pile et les fonctions elementaires de la pile

--------------------------------------------------------------------"""

class Pile:
    """
    Rôle    : Crée la classe de la pile
    """

    def __init__(self):
        """
        Rôle    : Initialise la pile
        Entré   : Rien
        Sortie  : Rien
        """

        self.elems = []


    def __len__(self):
        """
        Rôle    : Calcul la taille de la pile
        Entré   : Rien
        Sortie  : La taille de la pile (int >=0)
        """
        
        # retourne le nombre d'élément dans la pile
        return len(self.elems)


    def __str__(self) :
        """
        Rôle     transforme la pile en chaine de caractère
        Entré   : Rien
        Sortie  : la chaine de la caractère qui represente la pile (str)
        """

        return str(self.elems)


    def __repr__(self) :
        """
        Rôle    : affiche la représentation de la pile en chaine de caractère
        Entré   : Rien
        Sortie  : la représentation de la pile (str)
        """

        return str(self)


    def isEmpty(self):
        """
        Rôle    : Vérifie si la pile est vide
        Entré   : Rien
        Sortie  : Si la pile est vide (bool)
        """

        # si la pile n'a pas d'élément
        if len(self)==0:
            empty = True

        # si la pile a des éléments
        else:
            empty = False

        return empty


    def popElem(self):
        """
        Rôle    : Retire un élement de la pile
        Entré   : Rien
        Sortie  : L'élement qui a été retiré de la pile
        """

        # si la pile est vide envoyer une erreur
        assert not self.isEmpty()

        # retire un élement et le retourne
        return self.elems.pop()

        


    def pushElem(self,value):
        """
        Rôle    : Ajoute un élement de la pile
        Entré   : L'élément à ajouter
        Sortie  : Rien
        """

        # ajoute un élement
        self.elems.append(value)


#---------------------------------------------------------------------------
# TEST
#---------------------------------------------------------------------------

if __name__ == '__main__':
    test = Pile()

    print(test.isEmpty(),"\n")

    test.pushElem(7)
    test.pushElem(3)
    print(test,"\n")

    test.pushElem(4)
    print(test,"\n")

    print(test.popElem())
    print(test,"\n")

    print(len(test),"\n")

    print(test.isEmpty())