import os
from PIL import Image
import time
import cv2
import shutil

from zzpath import *
from liste_traitement import *
from opération_dossier import *
from traitement_image import *
from attention_visuelle import *
from définition import *

class Main:


    def mysql_connexion(self):
        pass


    def creation_dossier(self):
        
        Dossier.se_placer(self, DOSSIER_TEST)
        Dossier.creation_dossier_test(self)
        Dossier.crea(self, FORME_GEO, NOM_GEO)
        Dossier.crea(self, PATH_DOSSIER_PY, NOM_DEF)

    def rognage_ciel(self):
        """ on prend le haut des images d'un dossier,et on extrait les
            couleurs prncipales."""

        Dossier.se_placer(self, PATH_DOSSIER_PY)

        Dossier.move_fichier(self, IMAGE, PATH_CIEL)       
        Dossier.move_fichier(self, FICHIER_ZTEST, PATH_CIEL)
        Dossier.move_fichier(self, FICHIER_Z_COUL_CIEL, PATH_CIEL)                 
        
    #1
        Traitement_image.rognage_des_ciels(self, PATH_CIEL, TOP_CIEL_DOSSIER,
                                    HAUTEUR_CIEL_DOSSIER, FICHIER_Z_COUL_CIEL,
                                           DOSSIER_TEST)


    #2
        Traitement_image.rognage_ciel(self, IMAGE, NOM_SAVE_CIEL, HEIGHT,
                                     TOP_CIEL, FICHIER_ZTEST)
        
    #3
        Traitement_image.couleur(self, NOM_SAVE_CIEL, FICHIER_ZTEST)

    #a   
        liste_traitement.occurence_ciel(self, IMAGE, FICHIER_Z_COUL_CIEL,
                                        FICHIER_ZTEST) 

        Dossier.move_fichier(self, IMAGE, PATH_DOSSIER_PY)
        Dossier.move_fichier(self, FICHIER_ZTEST, PATH_DOSSIER_PY)
        Dossier.move_fichier(self, FICHIER_Z_COUL_CIEL, PATH_DOSSIER_PY)


    def compa_couleur(self):

        Traitement_image.couleur_image(self, IMAGE, PATH_DOSSIER_PY, DOSSIER_TEST,
                                     PATH_DOSSIER_PY)
        
        Traitement_image.comparaison_des_couleurs(self, DOSSIER_TEST)

        
    def comparaison(self):
        
                
        Dossier.se_placer(self, PATH_DOSSIER_PY)

        Dossier.move_fichier(self, IMAGE, PATH_IMAGE)

    #4 et 5
        Traitement_image.comparage_sans_rognage(self, PATH_IMAGE, IMAGE,
                                        PATH_TEST1, FICHIER_ZTEST)
        
        Dossier.sous_doss(self, PATH_TEST1, DOSSIER_TEST)
    #6
        Traitement_image.comparage_rognage_des_images(self, PATH_IMAGE,
                                                    IMAGE, PATH_TEST2)

        Dossier.sous_doss2(self, PATH_TEST2, DOSSIER_TEST)

        Dossier.se_placer(self, PATH_DOSSIER_PY)


    def récapitulatif(self):

         
        liste_traitement.liste_test(self, PATH_TEST1)
        liste_traitement.liste_test(self, PATH_TEST2)

        Dossier.se_placer(self, PATH_DOSSIER_PY)
        Dossier.effacage(self, ZTEST, ZTEST_COPIE, DOSSIER_TEST)
        Dossier.exportation(self, ZTEST1, ZTESTDOSS1)
        Dossier.exportation(self, ZTEST2, ZTESTDOSS2)

        
    def découpage_photo(self):

        
       Dossier.se_placer(self, PATH_DOSSIER_PY)
       Découpage.découpe(self, IMAGE, 5, 5, FORME_GEO)


    def définition(self):
        
       déf.effillage(self, PATH_DEF, PATH_DOSSIER_PY)



if __name__ == "__main__":

    main = Main()
    #main.creation_dossier()
    #main.rognage_ciel()
    #main.compa_couleur()
    #main.comparaison()
    #main.récapitulatif()
    #main.découpage_photo()
    main.définition()









    
