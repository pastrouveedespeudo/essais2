from path import *
import os


class fichier:

    def requete_py(self, fichier, element, liste):

        self.fichier = fichier
        self.element = element
        self.liste = liste
        
        with open(str(self.fichier),"w", errors = "ignore") as file:
            file.write(str(self.element))
                        
        with open(self.fichier,"r") as file2:
            b = file2.read()

        self.liste.append(b)

    
    def modele(self, liste):
        self.liste = liste
        
        with open(FICHIER_PHRASE,"r", encoding = "utf-8") as file:
            a = file.read()

        self.liste.append(a)    


    def ecriture_phrase(self, liste1):

        liste = []
        liste2 = []

        self.liste1 = liste1

        with open(QUESTION,"r", encoding = "utf-8") as file:
            a = file.read()

        liste.append(a)

        liste2 = liste[0][:-2]
  
        with open(QUESTION, "w", encoding = "utf-8") as file:
            file.write(str(liste2))

        with open(QUESTION, "a", encoding = "utf-8") as file:
            file.write(",")
            file.write("\n")
            file.write("            ")
            file.write(str(self.liste1))
            file.write(" ]")

    def lecture(self, liste):
        self.liste = liste
        
        with open(QUESTION,"r", encoding = "utf-8") as file:
            a = file.read()
            print(file.read())
        self.liste.append(a)
        

    def fichier(self, direction):

        self.direction = direction
                
        os.chdir(self.direction)

        #a appeler 2 fois

















        



            
