"""--------------------------------------------------------------------

Auteur  :   Nathan GUYARD
Date    :   01/03/2023
Rôle    :   créent les différentes langues et les dictionnaires

--------------------------------------------------------------------"""
from Langue import *

# crée un dictionnaire contenant toutes les langues
LANGUAGE_ABR = {
    "francais":Language("francais"),
    "allemand":Language("allemand"),
    "anglais":Language("anglais"),
    "espagnol":Language("espagnol"),
    "italien":Language("italien"),
    "neerlandais":Language("neerlandais")
}