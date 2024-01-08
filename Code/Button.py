"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   18/12/2022
Role    :   implemente les bouttons

--------------------------------------------------------------------"""
from screenPygame import*

class Button:
    """
    Role    : Crée un Boutton
    """
    
    def __init__ (self,x,y,width,height,img = None,scale=1):
        """
        Rôle    : Initialise le boutton
        Entré   : coordonnée x (int) ,coordonnée x (int) ,largeur (int), longueur (int), image (str), échelle (int)
        Sortie  : Rien
        """
        
        # stock la position et la largeur du boutton+
        self.pos = (x,y)
        self.height = int(height * scale)
        self.width = int(width * scale)
        
        #verifi si il le boutton a une image
        if img != None:
            # stock l'image
            self.img = pygame.image.load(img)
            self.img = pygame.transform.scale(self.img, (self.width,self.height))
        else:
            self.img = None
        
    def isClic (self,pos):
        """
        Rôle    : Vérifie si le boutton est cliquer
        Entré   : position x,y du clic (list/tuple)
        Sortie  : si le boutton est cliquer (bool)
        """

        clic = False
        
        # vérifi la colision avec le boutton
        if pos[0] >= self.pos[0] and pos[0] <= self.pos[0] +self.width and pos[1] >= self.pos[1] and pos[1] <= self.pos[1] + self.height:
            clic = True
        
        return clic
    
    
    def load (self):
        """
        Rôle : Affiche le boutton
        Entré : Rien
        Sortie : Rien
        """
        
        if self.img != None:
            # affiche le boutton
            SCREEN.blit(self.img,self.pos)
            
            
            