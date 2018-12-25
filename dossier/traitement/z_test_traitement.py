from shutil import *
import os


class zcoul:

    def __init__(self):
        
        Mysql.connexion(self)


    def ouvrir(self, fichier):

        self.fichier = fichier

        liste = []
        
        with open(self.fichier,"r") as file:
            for i in file :
                liste.append(i)

                

    def occurence(self, dossier, dossier_image, nom, image):


        user = "jbaw"

        self.dossier_image = dossier_image
        self.dossier = dossier
        self.nom = nom
        self.image = image
        
        liste_travailler = []
        
        os.chdir(self.dossier)
        liste = os.lisdir(".")

        for i in liste:
            liste_travailler.append(i[:-4])
            
            
        liste_travailler.sort()

        voiture = liste_travailler[:13]
        tram = liste_travailler[13:25]
        panneau = liste_travailler[ 26: 49]
        immeuble = liste_travailler[50:76]

        se_placer(self, self.dossier_image)
             
        for i in liste_travailler:

            if i in range(1, 13):
 
                self.cursor.execute("""

                INSERT INTO image_ciel
                (categorie, nom, image)
                VALUES (%s, %s),"""
                (voiture, self.nom, self.image) )
                self.connexion.commit()
                
            elif i in range(13, 25):

                self.cursor.execute("""

                INSERT INTO image_ciel
                (categorie, nom, image)
                VALUES (%s, %s),"""
                (tram, self.nom, self.image) )
                self.connexion.commit()


            elif i in range(26, 49):

                self.cursor.execute("""

                INSERT INTO image_ciel
                (categorie, nom, image)
                VALUES (%s, %s),"""
                (panneau, self.nom, self.image) )
                self.connexion.commit()


            elif i in range(50, 76):

                self.cursor.execute("""

                INSERT INTO image_ciel
                (categorie, nom, image)
                VALUES (%s, %s),"""
                (immeuble, self.nom, self.image) )
                self.connexion.commit()
                
                
                

                




























            
           
