import os
from PIL import Image
import time
import cv2
import shutil

from zzpath import *
from zcouleur_ciel import *
from liste_traitement import *
from opération_dossier import *
from traitement_image import *




class Main:
    

    
    def fonction_outil(self):

        Dossier.se_placer(self, PATH_DOSSIER_PY)#ciel

        Dossier.copie_move(self)


    def ouverture(self):

        
        
        Dossier.copie_fichier(self, image, image_copie)
        
        Dossier.copie_fichier(self, fichier_ztest, fichier_ztest_copie)
        
        Dossier.copie_fichier(self, fichier_z_coul_ciel,
                              fichier_z_coul_ciel_copie)


   
        

    def rognage_ciel(self):

 
        Dossier.move_fichier(self, image_copie, path_ciel)#zzz into ciel
        
        Dossier.move_fichier(self, fichier_ztest_copie, path_ciel)#ztest ciel
        Dossier.move_fichier(self, fichier_z_coul_ciel_copie,
                             path_ciel)#sliste ciel

        
        Dossier.se_placer(self, path_ciel)#ciel
        
        Traitement_image.rognage_ciel(self, image_copie,
                                            nom_save_ciel,
                                            100,
                                            top_ciel,
                                            fichier_ztest_copie)
        
        Traitement_image.couleur(self, nom_save_ciel, fichier_ztest_copie)
        liste_traitement.occurence_ciel(self, image_copie,
                                        liste_couleur_ciel,
                                        fichier_ztest_copie)
        
        Dossier.move_fichier(self, image_copie, path1_racine)#zzz into ste fois

        Dossier.move_fichier(self, fichier_ztest_copie,
                             path1_racine)#ztest/ste fois
        
        Dossier.move_fichier(self, fichier_z_coul_ciel_copie,
                             path1_racine)#sliste/ste fois
        
        Dossier.se_placer(self, path1_racine)#ste fois

    
    def comparaison(self):
        
        Dossier.se_placer(self, path1_racine)#ste fois
        Dossier.move_fichier(self, image_copie, path_image)#zzz into les images
        
        Dossier.se_placer(self, path_image)#image
        
        Traitement_image.comparage_sans_rognage(self,
                                                path_image,
                                                image_copie) # image

        time.sleep(2)
        
        Dossier.move_fichier(self, image_copie, path_image)#zzz into les images
        
        Dossier.se_placer(self, path1_racine)#ste fois
        Dossier.se_placer(self, path_image)#les images
        
        Traitement_image.comparage_rognage_des_images(self, image_copie,
                                                      path_image,
                                                      path_image,)
        
        Dossier.move_fichier(self, image, path1_racine)#zzz into ste fois
        Dossier.se_placer(self, path1_racine)#ste fois


    def récapitulatif(self):

        
        Dossier.se_placer(self, path1_racine)#ste fois
        Dossier.move_fichier(self, fichier_ztest, path_image)#ztest/image
        Dossier.se_placer(self, path_image)#ste image
        
        liste_traitement.récapitulatif(self, path_image)   

        Dossier.move_fichier(self, fichier_ztest, path_image)#ztest/ste fois
        
        Dossier.se_placer(self, path1_racine)#ste fois
        Dossier.se_placer(self, path_image)
        
        move_fichier(self, fichier_z_coul_ciel, path_image)

        Dossier.se_placer(self, path_image)
        liste_traitement.lecture(self, fichier_z_coul_ciel)
        
        move_fichier(self, fichier_z_coul_ciel, path1_racine)
        move_fichier(self, fichier_ztest, path1_racine)
        
    def question_finale_qui_doit_etre_un_autre_fichier(self):

        pass




if __name__ == "__main__":

    main = Main()
    #main.copie_move()
    main.ouverture()
    #main.rognage_ciel()
    #main.comparaison()
