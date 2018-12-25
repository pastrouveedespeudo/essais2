from opération_dossier import *
from zzpath import *


class fonction_outil:


    def fonction_outil(self):

        Dossier.se_placer(self, PATH_DOSSIER_PY)
         
        Dossier.copie_fichier(self, "aimmeuble.py", "aimmeuble2.py")
        Dossier.move_fichier(self, "aimmeuble2.py", PATH_DOSSIER_PY)
        
        
        Dossier.copie_fichier(self, "avoiture.py", "avoiture2.py")
        Dossier.move_fichier(self, "avoiture2.py", PATH_DOSSIER_PY)
        
        
        Dossier.copie_fichier(self, "apanneau.py", "apanneau2.py")
        Dossier.move_fichier(self, "apanneau2.py", PATH_DOSSIER_PY)
        
        
        Dossier.copie_fichier(self, "atram.py", "atram2.py")
        Dossier.move_fichier(self, "atram2.py", PATH_DOSSIER_PY)

        print("tout les dossiers sont copié et mis dans la racine")

if __name__ == "__main__":
    

    yo = fonction_outil()
    yo.fonction_outil()
