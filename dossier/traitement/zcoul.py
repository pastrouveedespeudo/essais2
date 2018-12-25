class zcoul:

    def __init__(self):
        pass


    def ouvrir(self, fichier):

        self.fichier = fichier

        liste = []
        
        with open(self.fichier,"r") as file:
            for i in file :
                liste.append(i)
            



    def occurence(self):
        pass
