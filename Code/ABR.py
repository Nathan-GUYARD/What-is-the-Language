"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   implemente l'arbre binaire de recherche (ABR)

--------------------------------------------------------------------"""
class ABR:
    """
    Role    : Crée un ABR
    """
    
    def __init__(self,value):
        """
        Rôle    : Initialise l'arbre
        Entré   : valeur de la racine (str)
        Sortie  : Rien
        """

        # initialise les attributs de l'ABR
        self.left = None
        self.right = None
        self.value = value
        

    def insert(self,value):
        """
        Rôle    : insere dans l'arbre un élement
        Entré   : valeur (str)
        Sortie  : Rien
        """

        temp = self
        isInsert = False
        # tant que la valeur n'est pas inseré
        while not isInsert:
            # si la valeur est déjà présente dans l'arbre
            if value == temp.value:
                isInsert = True
            
            # si la valeur à inseré est plus petite que le noeud visité
            elif value < temp.value:
                # si le noeud à un noeud gauche
                if temp.left != None:
                    # va à gauche
                    temp = temp.left
                else:
                    # insere la valeur
                    temp.left = ABR(value)
                    isInsert = True
            
            else :
                # si le noeud à un noeud droit
                if temp.right != None:
                    # va à droite
                    temp = temp.right

                else:
                    # insere la valeur
                    temp.right = ABR(value)
                    isInsert = True


    def insertAll(self,tab):
        """
        Rôle    : insere dans l'arbre tout les élements du tableau
        Entré   : tableau de valeur (list)
        Sortie  : Rien
        """

        # inserer chaque element de la liste
        for value in tab:
            self.insert(value)


    def parcourInf(self):
        """
        Rôle    : Effectue le parcour infixe de l'arbre
        Entré   : Rien
        Sortie  : 
        """

        # si l'arbre il n'y a pas d'arbre gauche et d'arbre droit
        if self.left == None and self.right == None:
            # le tableau est égal à la valeur du neoud
            tab = [self.value]

        # si l'arbre il n'y a pas d'arbre droit
        elif self.right == None:
            # execute la fonction parcours Infixe sur l'arbre gauche et ajoute la valeur du neoud
            tab = self.left.parcourInf() + [self.value]

        # si l'arbre il n'y a pas d'arbre gauche
        elif self.left == None:
            # le tableau est égal à la valeur du neoud et ajoute l'execution de la fonction parcours Infixe sur l'arbre gauche
            tab = [self.value] + self.right.parcourInf()

        # si l'arbre il y a un arbre gauche et un arbre droit
        else:
            # execute la fonction parcours Infixe sur l'arbre gauche, ajoute la valeur du neoud puis execute la fonction parcours Infixe sur l'arbre droit
            tab = self.left.parcourInf() + [self.value] + self.right.parcourInf()

        return tab


    def parcourPre(self):
        """
        Rôle    : Effectue le parcour préfixe de l'arbre
        Entré   : Rien
        Sortie  : 
        """

        # si l'arbre il n'y a pas d'arbre gauche et d'arbre droit
        if self.left == None and self.right == None:
            # le tableau est égal à la valeur du neoud
            tab = [self.value]

        # si l'arbre il n'y a pas d'arbre droit
        elif self.right == None:
            # le tableau est égal à la valeur du neoud et ajoute l'execution de la fonction parcours Infixe sur l'arbre droit
            tab = [self.value] + self.left.parcourPre() 

        # si l'arbre il n'y a pas d'arbre gauche
        elif self.left == None:
            # le tableau est égal à la valeur du neoud et ajoute l'execution de la fonction parcours Infixe sur l'arbre gauche
            tab = [self.value] + self.right.parcourPre()

        # si l'arbre il y a un arbre gauche et un arbre droit
        else:
            # le tableau est égal à la valeur du neoud, ajoute l'execution de la fonction parcours Infixe sur l'arbre gauche puis ajoute l'execution de la fonction parcours Infixe sur l'arbre droit
            tab = [self.value] + self.left.parcourPre() + self.right.parcourPre()
    
        return tab


    def parcourSuf(self):
        """
        Rôle    : Effectue le parcour suffixe de l'arbre
        Entré   : Rien
        Sortie  : 
        """

        # si l'arbre il n'y a pas d'arbre gauche et d'arbre droit
        if self.left == None and self.right == None:
            # le tableau est égal à la valeur du neoud
            tab = [self.value]

        # si l'arbre il n'y a pas d'arbre droit
        elif self.right == None:
            # execute la fonction parcours Infixe sur l'arbre gauche et ajoute la valeur du neoud
            tab = self.left.parcourSuf() + [self.value]

        # si l'arbre il n'y a pas d'arbre gauche
        elif self.left == None:
            # execute la fonction parcours Infixe sur l'arbre droit et ajoute la valeur du neoud
            tab = self.right.parcourSuf() + [self.value]

        # si l'arbre il y a un arbre gauche et un arbre droit
        else:
            # execute la fonction parcours Infixe sur l'arbre gauche, puis execute la fonction parcours Infixe sur l'arbre droit et ajoute la valeur du neoud
            tab = self.left.parcourSuf() + self.right.parcourSuf() + [self.value]

        return tab


    def parcourLarg(self):
        """
        Rôle    : Effectue le parcour en largeur de l'arbre
        Entré   : Rien
        Sortie  : 
        """
        
        # crée la file contenant la racine
        queue = [self]
        tab = []
        
        while len(queue) != 0:
            # vide la file
            noeud = queue.pop(0)
            
            # ajoute la valeur du noeud au tableau
            tab.append(noeud.value)
            
            # ajoute l'arbre gauche à la file
            if noeud.left != None:
               queue.append(noeud.left)
               
            # ajoute l'arbre droit à la file
            if noeud.right != None:
               queue.append(noeud.right)
        
        return tab


    def __len__(self):
        """
        Rôle    : Calcul la taille de l'arbre
        Entré   : Rien
        Sortie  : taille de l'arbre
        """
        
        # calcule la taille de l'arbre sans fils
        if self.left == None and self.right == None:
            taille = 1
        
        # calcule la taille de l'arbre gauche
        elif self.left == None:
            taille = 1 +  len(self.right)
        
        # calcule la taille de l'arbre droit
        elif self.right == None:
            taille = 1 + len(self.left)
        
        # calcule la taille de l'arbre
        else:
            taille = 1 + len(self.left) + len(self.right)
    
        return taille

    def height(self):
        """
        Rôle    : Calcul la hauteur de l'arbre
        Entré   : Rien
        Sortie  : hauteur de l'arbre (int)
        """
        
        # calcule la hauteur de l'arbre gauche
        heightleft = -1
        if self.left != None:
            heightleft = self.left.height()
        
        # calcule la hauteur de l'arbre droit
        heightright = -1
        if self.right != None:
            heightright = self.right.height()
        
        #calcule la hauteur de l'arbre
        if heightleft >= heightright:
            height = 1 + heightleft
        else:
            height = 1 + heightright
    
        return height

    def isInABR(self,value):
        """
        Rôle    : Cherche une valeur dans l'ABR
        Entré   : valeur rechercher (str)
        Sortie  : vari si il existe
        """

        # traite l'arbre sans noeud
        if self == None:
            bool =  False
        
        # retourne vrai si la valeur chercher est la bonne
        elif self.value == value:
            bool = True
        
        # traite l'arbre gauche si la valeur du noeud est plus grand que la valeur rechercher
        elif self.value > value:
            if self.left != None:
                bool = self.left.isInABR(value)
            
            else:
                bool = False
            
        # traite l'arbre droit si la valeur du noeud est plus petit que la valeur rechercher
        else:
            if self.right != None:
                bool = self.right.isInABR(value)
            else:
                bool = False

        return bool