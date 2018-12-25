from path import *

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

