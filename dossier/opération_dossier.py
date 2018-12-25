import os
import shutil
from zzpath import *

class Dossier:

    def creation_dossier_test(self):
        """ on prend le dernier fichier, on prend le dernier numero
        on ajout un"""
        
        liste = os.listdir()
        liste_el = []
                    
        for i in liste:
            liste_el.append(i)
       
        self.nom_doss = liste_el[-1][-1]
        self.nom_doss = int(self.nom_doss)
        self.nom_doss = self.nom_doss + 1
        self.nom_doss = str(self.nom_doss)
        self.nouveau = "dossier" + self.nom_doss
        os.mkdir(self.nouveau)

    def creation_doss_rognages_ciels(self, dossier, fichier):

        self.dossier = dossier
        self.ficheir = fichier
        
        os.chdir(self.dossier)
        liste = os.listdir(".")
        mettre_fichier = liste[-1]

        os.move(self.fichier, mettre_fichier)



    def se_placer(self, dossier):

        self.dossier = dossier
        os.chdir(self.dossier)

    def liste_dossier(self):

        liste = os.listdir(".")
        print(liste)

    def supprimer_un(self, fichier):

        self.fichier = fichier
        
        with open(self.fichier) as file:
            print("il existe")
            file.close()
            os.remove(file)

            
    def supprimer_un_sans_test(self, fichier):

        self.fichier = fichier
        os.remove(self.fichier)      


    def supprimer(self):

        liste = os.listdir(".")
        for i in liste:
            os.remove(i)


    def move_fichier(self, fichier, dossier):

        self.fichier = fichier
        self.dossier = dossier
        
        shutil.move(self.fichier, self.dossier)
        
            

    def creation_dossier(self, dossier):

        self.dossier = dossier
    
        os.mkdir(self.dossier)  


    def pass_fichier_py(self, i):

        self.i = str(i)
        
        if self.i == i + ".py":
            pass
        
    def copie_fichier(self, fichier, copie_fichier):

        self.fichier = fichier
        self.copie_fichier = copie_fichier

        shutil.copy(self.fichier, self.copie_fichier)

    def pass_dossier(self, dossier):

        pass


    def effacage(self, fichier, fichier2, path):

        self.fichier = fichier
        self.fichier2 = fichier2
        self.path = path
        
        shutil.copy(self.fichier, self.fichier2)
        shutil.move(self.fichier2, self.path)

        fichier = open(self.fichier, "w")
        fichier.write(" ")
        fichier.close()

    def effacage_dossier(self, dossier):

        self.dossier = dossier

        liste = os.listdir(".")
        for i in liste:
            os.remove(i)
        

    def exportation(self, doss, dossier):

        self.doss = doss
        self.dossier = dossier
        os.chdir(self.doss)
        liste = os.listdir(".")
        for i in liste:
            shutil.move(i, self.dossier)




    def sous_doss(self, dossier, dossier_test):

        self.dossier = dossier
        self.dossier_test = dossier_test


        os.chdir(self.dossier_test)
        liste0 = os.listdir(".")
        endroit = liste0[-1]

        os.chdir(endroit)
        os.mkdir(
            r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}\test1".format(endroit))
        
        os.chdir(self.dossier)
        liste = os.listdir(".")
        for i in liste:
            shutil.move(i, r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}\test1".format(endroit))
            
    def sous_doss2(self, dossier, dossier_test):

        self.dossier = dossier
        self.dossier_test = dossier_test


        os.chdir(self.dossier_test)
        liste0 = os.listdir(".")
        endroit = liste0[-1]

        os.chdir(endroit)
        os.mkdir(
            r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}\test2".format(endroit))
        
        os.chdir(self.dossier)
        liste = os.listdir(".")
        for i in liste:
            shutil.move(i, r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}\test2".format(endroit))
            

    def dernier_doss(self, image, dossier, dossier2):
        
        self.dossier = dossier
        self.image = image
        self.dossier2 = dossier2
        
        os.chdir(self.dossier)
        liste = os.listdir(".")
        dernier = liste[-1]

        os.chdir(self.dossier2)
        
        shutil.move(self.image, r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}".format(str(dernier)))
            
            

#move ztest1 to dossier in dossier

    def move_fichier2(self, dossier, fichier):

        self.dossier = dossier
        self.fichier = fichier
        
        os.chdir(self.dossier)
        
        liste = os.listdir(".")
        dernier_dossier = liste[-2]
        print(dernier_dossier)
        
        dernier_dossier = str(dernier_dossier)
        shutil.move(self.fichier, dernier_dossier)
            
        
    def move_fichier3(self, dossier, fichier):

        self.dossier = dossier
        self.fichier = fichier
        
        os.chdir(self.dossier)
        
        liste = os.listdir(".")
        dernier_dossier = liste[-1]
        print(dernier_dossier)
        
        dernier_dossier = str(dernier_dossier)
        shutil.move(self.fichier, dernier_dossier)


    def crea(self, dossier, nom):

        self.dossier = dossier
        self.nom = nom

        os.chdir(self.dossier)
        os.mkdir(self.nom)


    def dernier_doss_test(self, dossier):

        self.dossier = dossier

        os.chdir(self.dossier)
        liste = os.listdir(".")
        dernier = liste[-1]
        path = r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}".format(dernier)
        
        


        


   



                     
