# -*- coding: utf-8 -*-
import requests

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

from fichier import *
from path import *

class internet:

    def search(self, mot, liste1):

        
        self.mot = mot
        
        self.liste1 = liste1
        self.liste = []

        path = DICO_DEF.format(self.mot)
        
        requete = requests.get(path)
        page = requete.content
        
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find_all("div", {"class":"defbox"})
        
        for i in propriete:
            fichier.requete_py(self, "requete.py", i, self.liste)
            pos1 = str(self.liste).find("<span>") + 3
            pos2 = str(self.liste).find("</span>") - 3
            a = self.liste[0][pos1:pos2]
            self.liste = []
            
            autre_def = str(i).find("Autre définition")
            autre_def1 = str(i).find("Aucun mot trouvé")

            if autre_def > 0:
                pass
            
            elif autre_def1 > 0:
                pass
            
            elif a == "Définitions corespondante à votre recherche":
                mot_sing = mot[:-1]
                mot_trouvé = str(propriete).find(str(mot_sing))
                mot_fem_plur = mot[:-2]
                mot_fem_plur_trouvé = str(propriete).find(str(mot_fem_plur))
                
                if mot_trouvé > 0:                                  #sing
                    path_sing = DICO_DEF.format(str(mot_sing))
                    requete = requests.get(path_sing)
                    page = requete.content
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find_all("div", {"class":"defbox"})

                    for i in propriete:
                        fichier.requete_py(self, "requete.py", i, self.liste)
                        pos1 = str(self.liste).find("<span>") + 3
                        pos2 = str(self.liste).find("</span>") - 3
                        a = self.liste[0][pos1:pos2]
                        mot_trouvé2 = str(a).find(str("Autre définition"))
                                                                                    #plur fem
                        if a == "Définitions corespondante à votre recherche"\
                           and mot_fem_plur_trouvé > 0:
                            path_fem = DICO_DEF.format(str(mot_fem_plur))
                            requete = requests.get(path_fem)
                            page = requete.content
                            soup = BeautifulSoup(page, "html.parser")      
                            propriete = soup.find_all("div", {"class":"defbox"})

                            for i in propriete:
                                #print(i)
                                fichier.requete_py(self, "requete.py", i, self.liste)
                                pos1 = str(self.liste).find("<span>") + 3
                                pos2 = str(self.liste).find("</span>") - 3
                                a = self.liste[0][pos1:pos2]
                                if a == "Définitions corespondante à votre recherche":
                                    pass
                                else:
                                    self.liste1.append(a)
                                self.liste = []
                                
                        elif mot_trouvé2 > 0:
                            pass
                        else:
                            self.liste1.append(a)
                            self.liste = []
                    
                        
            else:
                self.liste1.append(a)

        
        self.liste1 = set(self.liste1)
    #fais une fonction pour les pavés
    #régler les apostrophes
    #apprendre les framework et effacer toutes ces lignes...
        
    def search_verbe(self,path, recherche, liste, fichier, mode, mode2):
        
        self.path = path 
        self.recherche = recherche
        self.liste = liste
        self.fichier = fichier
        self.mode = mode
        self.mode2 = mode2

        path_verbe = DICO_VERBE.format(str(self.recherche))
        requete = requests.get(path_verbe)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find("blockquote")

        with open(self.fichier, self.mode) as file:
            file.write(str(propriete))
                    
        with open(self.fichier, self.mode2) as file2:
            b = file2.read()

        pos1 = str(b).find("VERBE")
        
        if pos1 > 0:
            self.liste.append("Verbe")
        
        else:
            self.liste.append("None")










        
            if self.oInput[-1] == "?":
                nom_phrase = "phrase interogrative"
                self.liste_melange.insert(0, nom_phrase)
            
            elif self.oInput[-1] == "!":
                nom_phrase = "phrase exclamative"
                self.liste_melange.insert(0, nom_phrase)

            else:
                nom_phrase = "phrase " + str(self.liste_melange[0])
                self.liste_melange.insert(0, nom_phrase)
