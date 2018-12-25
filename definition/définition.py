"""definition de l'objet"""
import random
import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import re
import shutil
import os



class déf:

       def effillage(self):
              
              self.liste3 = []
              liset = []
              liste2 = []
              os.chdir(r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1")
              liste = os.listdir(".")
              dernier = liste[-1]
              os.chdir(r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}\test1".format(dernier))      
              liste1 = os.listdir(".")
              for i in liste1:
                     for a in i:
                            if a != "." and a!= "p" and a != "j" and a != "g":
                                   liset.append(a)
                            a = "".join(liset)
                            
                     liste2.append(int(a))

                     for i in liste2:
                            if i <= 13:
                                   self.liste3.append("immeuble")
                            elif i > 13 and i <= 25:
                                   self.liste3.append("panneau")
                            elif i > 26 and i <= 49 :
                                   self.liste3.append("tram")
                            elif i > 50:
                                   self.liste3.append("voiture")
              
                                   
              self.liste3 = set(self.liste3)


                     #fais une fonction car sa limite les dossiers

              
       def dictionnaire_en_ligne(self,dossier_def):

              self.dossier_def = dossier_def

              for i in self.liste3:
       
                     self.lien = "http://www.le-dictionnaire.com/definition.php?mot={}".format(i)
                     requete = requests.get(self.lien)
                     page = requete.content
                     soup = BeautifulSoup(page, "html.parser")

                     definition_mot = "definition {}".format(i)
                     defi_mot = soup.find_all("div", {'class':"defbox"})
                     
                     defi_mot = str(defi_mot)
                     liste = os.listdir(".")

                     nom_fichier = i +'.html'
                     with open(nom_fichier,"a") as file:
                            file.write(defi_mot)
                            
                     shutil.move(nom_fichier, self.dossier_def)

              
défi = déf()
défi.effillage()
défi.dictionnaire_en_ligne(r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier\définitions")

#creer un dossier avec les fichire python

