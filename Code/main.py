"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   lance le jeu

--------------------------------------------------------------------"""

from Menu import*

def main ():
    """
    Rôle    : Crée la fonction qui permet de lancer le jeu
    Entré   : Rien
    Sortie  : Rien
    """

    # crée le menu
    game = Menu()
    
    end = False
    while not end:
        # affiche la partie
        game.load()

        # récupère les input
        event = pygame.event.poll()
        # vérifi si les bouttons sont cliqués
        game.buttonsIsClic(event)
        
        # affiche toutes les modifications
        pygame.display.flip()

        # si la croix en cliqué
        if event.type == pygame.QUIT :
            # met fin a la boucle principale
            end = True
            # ferme la fenetre
            quit()

main()
