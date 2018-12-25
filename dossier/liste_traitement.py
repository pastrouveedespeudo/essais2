import os

from traitement_image import *


class liste_traitement:
    
    """on va regarder les couleurs de fichier d'un dossier,
        et comaprer ces couleurs avec notre image de départ"""
    
#a
    def occurence_ciel(self, image, fichier_ciels, fichier):

        Traitement_image.couleur(self, image, fichier)
        #on prend les couleurs de notre image

        self.fichier = fichier
        self.image = image
        self.fichier_ciels = fichier_ciels

        liste = []

        for clé, valeur in self.dico_couleur_ct.items():
            liste.append( (clé, valeur) )
            
        # on parcours le fichiers des ciels
        fichier = open(fichier_ciels, "r")
        compteur = 0
        
        try :
            for i in fichier :
                
                # on compare le nombre occurence
                liste, i[compteur] = set(liste), set(i[compteur])
                occurence = liste.intersection(i[compteur])
                a = str(i)
                
                with open(a, "a") as test:
                    test.write("\ncouleur commun: ")
                    test.write("i et ")
                    test.write(self.image)
                    test.write("\n")
                    test.write(str(occurence))
                    test.write("\n")
                    test.close()
                    
                compteur += 1
                
        except:
            pass


    def récapitulatif(self, dossier):
        
        self.dossier = dossier
        
        a = len(liste_dossier) -1
        b = liste_dossier[a]
        b = str(b)
        
        liste_dossier = os.listdir(".")

        for i in liste :

            c = 0
            while c < len(liste_dossier):

                Dossier.se_placer(self, i)
                
                with open(b) as file:

                    print("dans cette image il y a:", liste)
                    file.close()
                    
                c += 1

        print("les truk bizard c la couleur du haut et du bas ")



            
    def lecture(self, dossier):

        self.dossier = dossier
        with open(self.dossier,"r") as file:
            print(file)
            file.close()



    def recap(self, fichier):

        self.fichier = fichier
        
        file = open(self.fichier,"r")
        for i in file :

            print(i)



# -1

    def liste_test(self, dossier):

        self.dossier = dossier
        
        os.chdir(self.dossier)
        file = os.listdir(".")
        compteur = 0

        for i in file:

            compteur += 1
            

        print("dans ce fichier il y a", compteur)
        
        print(" de 1 a 13 : immeuble"
              " de 13 a 25 : panneau"
              " de 26 a 49 : tram"
              " de 50 a 76: voiture")

#ecrire ca dans un fichier
        































    
