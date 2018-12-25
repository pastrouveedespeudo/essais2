# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from path import *
from fichier import *
import urllib.request
import json
from PIL import Image

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



    def temps_verbe(self, recherche):

        self.recherche = recherche
        
        liste = []
        liste2  =[]
        
        path_verbe = DICO_VERBE.format(str(self.recherche))
        requete = requests.get(path_verbe)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find_all("table")

        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)
        
        a = str(liste).find(str(str(self.recherche)))
        if a > 0:
            liste2.append(liste[0][a - 600:a+20])
            b = str(liste2).find(str(str('<a href="#">')))
            liste3 = liste2[0][b+2:-250]

            c = str(liste3).find(str('</a>'))
            d = str(liste3).find(str('#">'))
            print(liste3[d + 3:c])


    def recherche_image(self, mot_cle, mot_cle1):
        #nom commun + adjectif
        
        self.mot_cle = mot_cle
        self.mot_cle1 = mot_cle1

        liste = []

        path =  "https://www.google.co.in/search?q={0}+{1}&source=lnms&tbm=isch"
        path1 = path.format(self.mot_cle, self.mot_cle1)
        requete = requests.get(path1)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find_all("img")
        
        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)


        for i in range(5):
            a = str(liste).find(str("src"))
            b = str(liste).find(str('" width='))
            
            url = liste[0][a+2:b-3]
            image = str("image_"+self.mot_cle+"_"+self.mot_cle1+str(i)+".jpg")

            liste[0] = liste[0][b:-3]

            urllib.request.urlretrieve(str(url), image)
            
            fichier.fichier(self, FICHIER_IMAGE)
            
        fichier.fichier(self, FICHIER_RACINE)
        #les stocker dans une base mysql
        #dans un autre fichier
        #greffer

        #appel fichier a tester
        


    def recherche_image_phrase(self, phrase):
        #nom commun + adjectif
        
        self.phrase = phrase

        liste = []

        path =  "https://www.google.co.in/search?q={0}&source=lnms&tbm=isch"
        path1 = path.format(self.phrase)
        requete = requests.get(path1)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find_all("img")
        
        with open("requete.py", "w") as file:
            file.write(str(propriete))
                    
        with open("requete.py", "r") as file2:
            b = file2.read()
        liste.append(b)


        for i in range(5):
            a = str(liste).find(str("src"))
            b = str(liste).find(str('" width='))
            
            url = liste[0][a+2:b-3]
            image = str("image_"+self.phrase+str(i)+".jpg")

            liste[0] = liste[0][b:-3]

            urllib.request.urlretrieve(str(url), image)
            
        #les stocker dans une base mysql
        #dans un autre fichier
        #greffer
        #appel fichier  a tester
            fichier.fichier(self, FICHIER_IMAGE)
        
        fichier.fichier(self, FICHIER_RACINE)

        
    def prenom(self, nom):

        self.nom = nom
        path = "https://www.prenoms.com/prenom/{}.html".format(self.nom)
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")  
        propriete = soup.find("title")
        a = str(propriete).find("Trouvez un prénom")
        if a < 0:
            print("prenom")
        else:
            print("pas prénom")



internet = internet()
internet.prenom("lea")












