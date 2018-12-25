import re
from bs4 import BeautifulSoup
import threading
from stock import *
import copy
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import html




class language: #dapres les resultats de images matchs page html

    def __init__(self):
        pass
    
    def liste_phrase(self):

        self.phrase = [ ["phrase_simple", "Sujet", "Verbe", "Nom commun"],
                        ["phrase_complexe", "sujet"]
                        ]
        #il faut les enrichir mais avant faut conjuguais les verbes
        #pour si on fait un input

        self.complement = ["Nom commun","Interjection","Adjectif"]


    def nettoyage(self):

        self.liste2 = []
        self.liste4 = []
        
        #ici ajouter le truk qui parcurs le dossier
        with open("voiture.html","r") as file:
            
            self.cleantext = BeautifulSoup(file, "lxml").text
        
        for i in self.cleantext:
            if i == "\n" or i == "[" or i == "]":
                pass
 
            else:
                self.liste2.append(i)

        self.liste2 = "".join(self.liste2)


    def ouverture(self):
        
        with open("file.py","w") as file:
            file.write(self.liste2)

        with open("file.py","r", encoding = "utf-8", errors = "ignore") as file:
            for i in file:
                self.liste4.append(i)
        
        
    def occurence(self):

        self.b = []
        self.laliste = []
        
        for i in self.complement:

            a = str(self.liste4).find(str(i))
            
            if a > 0:
                self.b.append(i)
        
        self.liste = []
        compteur = 0
        compteur2 = 0
        a = 0
        
        nombre_phrase = len(self.phrase)

        for i in self.phrase:
            for i in self.phrase[compteur]:

                self.liste.append(i)
                
                self.occurence2 = list(set(self.b) & set(self.liste))

                self.liste = []
                
                for i in self.occurence2:
                    compteur2 += 1
                    if compteur2 >= len(self.phrase[compteur]):
                        #vrai condition
                        type_phrase = self.phrase[compteur][0]
                        print("c'est une :", type_phrase)        
        compteur += 1        
        
        

        
    def text(self):

        self.text = ["["]
        
        with open("file.py","r", encoding = "utf-8" , errors = "ignore") as file:
            for i in file:
                for a in i:
                    if a != ".":
                        self.text.append(a)
                    elif a == ".":
                        self.text.append("],[")

        self.text.append("]]")
             
        self.text = "".join(self.text)
        self.text = self.text.replace(self.text[-5:-1], "")

        
    def fais_liste(self):

        
        compteur = 0
        compteur1 = 0
        self.liste = []
        self.liste2 = []
        for i in self.text:

            if i == "[":
                self.liste.append("[" + " ' ")
            elif i == ". ]":
                pass
            elif i == "]":
                self.liste.append("'" + "]")
            elif i ==  "],[" :
                self.liste.append("'" + "]" )
            
            else:
                self.liste.append(i)
                
            compteur1 += 1
            
        self.liste = "".join(self.liste)
        self.liste = self.liste[:-2]
        
        with open("stock.py","w") as file:
            file.write(self.liste)


        for i in self.text[11:]:
            self.liste2.append(i)
            
            #if i == "]":
                #self.liste2 = "".join(self.liste2)
                #print(self.liste2, "\n")
                
                #self.liste2 = []
                

    
    def remplissage_listee(self):

        
        compteur_index = 0
        compteur_liste = 0
        self.comptage = []
        
        #print(self.liste)
        
        for i in self.liste:
            if i == "]":
                compteur_liste += 1
                self.comptage.append(compteur_index)
            compteur_index +=1
            
        print(self.comptage)
        print("il faut", compteur_liste,"listes")


        self.liste_de_la_liste = [ [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
                                                   
        compteur1 = 0
        a = 0
        
        for i in self.liste:
            compteur1 += 1
            self.liste_de_la_liste[a].append(i)
            
            try:
                if compteur1 == self.comptage[a]:
                    a += 1

            except:
                pass


    def mot_phrase(self):


        a = 0
        b = []
        liste = []
        liste_phrase = []

        for i in self.complement:

            a = str(self.liste).find(str(i))
            if a > 0:
                b.append(i)
                
        comt = 0
        for i in b:
            for j in i:
                comt += 1
            comt = comt + 4

        
        for i in range(len(self.comptage)):
            
            self.liste_de_la_liste[i] = "".join(self.liste_de_la_liste[i])
            
            for j in self.liste_de_la_liste[i]:
                liste.append(j)
                liste_phrase.append(j)
                if j == " ":
                    liste = "".join(liste)
                    with open("dictionnaire.py","a") as file:
                        file.write("\n")
                        file.write(liste)
                    
                    
                    liste = []
                    liste = list(liste)
                    
                elif j == "]":
                    with open("phrase.py","a") as file:
                        liste_phrase = "".join(liste_phrase)
                        file.write(str(liste_phrase))
                        file.write("\n")
                        liste_phrase = list(liste_phrase)
                        liste_phrase = []



    def identification(self):


        liste1 = [ [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

        
        compteur = 0
        
        for i in self.liste_de_la_liste:
            for a in i :
                liste1[compteur].append(a)
                if a == "]":
                    compteur += 1#ici on met chaque ligne de la liste dans un des carrés
                                #mais on les met en lettre

        incrementeur = 0
        liste_tempo = []
        self.big_liste = []
        analyse_phrase = []
        sous_analyse_phrase = []
        
        for i in range(len(self.comptage)): #4fois
            for i in liste1[incrementeur]:      #on va faire mot par mot !                      
                liste_tempo.append(i)
                
                
                if i == " ":                    #on ajoute mot jusqua " "
                    mot = "".join(liste_tempo)  #on join le mot

                    path = "http://www.le-dictionnaire.com/definition.php?mot={}" 
                    
                    search = path.format(mot)
                    requete = requests.get(search)
                    page = requete.content

                    soup = BeautifulSoup(page, "html.parser")      
                    defi_mot = soup.find_all("div", {'class':"defbox"})
                    defi_mot = str(defi_mot) # on cherche le mot

                    liste5 = []#pour requete
                    liste6 = []#pour
                    
                    with open("requete.html","w") as file:      #on marque la def
                        file.write(str(defi_mot))

                    with open("requete.html","r") as file:
                        a = file.read()

                    liste5.append(str(a))                                   # on ajoute la def a la liste
                    balter = str(liste5).find(str("Aucun mot trouvé"))      #on cherche si ca dis nan
                    
                    if balter > 0:
                        print("encoder demande a kevin")
                                 #faut aussi enlever nom commun du début jlavais fais hier   
                    else:
                        pos1 = str(liste5).find("span>") + 2    #ok la tu sais pcque c cool
                        pos2 = str(liste5).find("</span") - 3
                        self.complement2 = liste5[0][pos1:pos2]    #oublie pas le .string c cool aussi
                                                            
                        sous_analyse_phrase.append(mot)
                        
                        for i in self.complement:
                            if i == self.complement2:       #on parcours notre liste complement
                                
                                print("c'est un : ",self.complement2)
                                analyse_phrase.append(self.complement2)
                                break
                            
                            elif self.complement2 == "Définitions corespondante à votre recherche":
                                print("non trouvé")
                                analyse_phrase.append("none type")
                                break                           #on compare avec le mot trouvé
                            
                            elif i != self.complement2:
                                
                                self.complement.append(i)
                                print("c'est un : ", self.complement2)
                                self.big_liste.append(self.complement2)
                                analyse_phrase.append(self.complement2)
                                break

                            elif self.complement2 == "Verbe":
                                language.les_verbes(self, mot)
                                
                        self.compltement = []#mot contenant nom commun ect

                    liste_tempo = [] #mot temporaire pour la recherche

                    
                                        
#----------------
            #ici il faut faire analyse
                    #avec anaylse_phrase et self.phrase
                    #mais faut rajouter des phrases

#----------------           
            
            #il faut nettoyer encore les mots

            print(analyse_phrase)
            print("\n")
            print("".join(sous_analyse_phrase)) #c les mots que l'on a cherché
            print("fin")
            
            incrementeur += 1   #enfete ici c plus pour marquer il faut faire analyse phrase
            analyse_phrase = [] #avant deffacer il faut stocker ca dans un fichier
                                #mais fais un pass
            sous_analyse_phrase = []#sert a montrer les mots
            
            time.sleep(2)



    def dico_complement(self):

        print(self.big_liste)       #on trie premier trie de la liste
        self.big_liste = set(self.big_liste)
        print(self.big_liste)
        
        #on sort de la boucle
        for i in self.big_liste:
            with open("complement.py","a") as file:
                file.write(i)
                file.write("\n")
                #on marque nos self.complement
                #cependant on va avoir des doublons a chaque essais...
                
        liste9 = []#il faut mettre ca la dedans pour supp les doublons
        with open("complement.py","r") as file:
            a = file.read()#cependant on va tout récuper en str il va falloir
                            #transformer, join et supp les doublons avec liste9 = set()
                            #on realité on va juste pass


    def temps(self):

        self.avant = []
        self.maintenant = []
        self.futur = []


    def les_verbes(self, mot):

        self.mot = mot
        liste_temps = []

        #self.mot = "etre"           #normalement on prend mot d'en haut
                                        #enelver le parametre et self.mot = mot
        
        path = "http://www.conjugaison.com/verbe/{}.html"
        
        #if self.complement2 == "Verbe":
            #search = path.format(mot)

        liste = []          #
        liste1 = []             # nous serve a travailler la page
        search = path.format(self.mot)
        requete = requests.get(search)
        page = requete.content
        
        soup = BeautifulSoup(page, "html.parser")      
        propriete = soup.find("blockquote") #on prend que le truk du haut

        print("ce verbe est un : ")
        for i in propriete:         #on prend que le truk du haut
            print(i)
            #enlever les br... .text.strip().string...

        propriete2 = soup.find("body").text #on prend le corps

        liste.append(propriete2)        #on lajourte dans une liste sinon on peut pas
                                    #faire de manip
        for i in liste:
            for a in i:                     #on fait une deuxime liste sans les saut
                if a != "\n":               #le faire dans la propre liste ca bug
                    liste1.append(a)
                else:
                   liste1.append(" ")
                   
        propriete3 = soup.find_all("td",{"class":"padding-bloc1"})  #on cherche que les paddin

        oContinuer = True
        c = 0
        liste1 = []
        liste2 = []
        while oContinuer:           
            try:
                print(propriete3[c].text)       #on print les paddin block par bloc <- nouvelle technique
                temps = str(propriete3[c]).find(str(self.mot))   #on trouve le mot parmis les paddin
                liste2.append(propriete3[c].text)
                temps2 = str(liste2).find(str(self.mot))
                
                if temps > 0:               #si on le trouve sinon ca passe au blok suivant
                    print(temps)    
                    for i in propriete3[c]:     #on prend le titre 
                        print(i.text)
                        liste1.append(i.text)
                        print("le verbe est conjuguai au:", str(liste1))
                    break
                    
                elif temps2 > 0:            #le site a 2 version
                    for i in propriete3[c]:       #on rajoute lhtml en mode text dans la liste
                        liste1.append(i.text)       #on recupere le titre depuis le premier if
                        print("le verbe est a :",liste1)
                    
                    break
                else:
                    print("le verbe est a l'infinit ou n'existe pas")
                    liste1.append("infinitif")

                c+=1
                time.sleep(1)   #<- sinon on attent
                liste_temps.append(liste1)
                liste1 = []     #<- on vide la liste
                liste2 = []
                print("\n\n")
                
            except:
                print("fini")
                break



#--------
 #raccorde ca a la structure d'avant
            
 #faire apprendre le temps !
            
 #il faudrait que ca comprenne enfete
            #imagerie mentale
            #image avec d'autre image
            #faut que ca apprenne
#------




    def proba(self):
        pass
    #si ca commence par ca alors on print(toutes les phrases (pour l'instant) )
    #et on fait proba


    def compréhension(self):


        #enfete la y faudrait ecrire dans fichier
        #prendre le fichier et le mettre dans la liste
        #DONC UNE LISTE
        #ex : liste = [[Psimple:,nom, verbe... Pcomplexe, nom, verbe, adj, Pexcla.. ... ... ! ect ]

        
        phrase_simple = ["Pronom", "Verbe", "Nom commun", "Adjectif"]
        phrase_simple1 = ["Forme d’article défini","Nom commun", "Verbe", "Adjectif"]
        
        phrase = [[],[]]
        
        liste_mot_sens = []
        liste_mot_sens2 = []
        
        liste = []

        
        oInput = input("rentre une phrase")
        #la voiture est rouge

        c = 0
        for i in oInput:
            liste[c].append(i)
            if i == " ":
                c += 1

        
        liste3 = []
        print(liste)
        for mot1 in liste:
            if mot1 == []:
                pass
            
            else:       
                path = "http://www.le-dictionnaire.com/definition.php?mot={}"#recherche pas verbe
                search = path.format("".join(mot1))

                requete = requests.get(search)
                page = requete.content
            
                soup = BeautifulSoup(page, "html.parser")      
                propriete = soup.find_all("div", {"class":"defbox"})


                for i in propriete:

                    with open("requete.py","w", errors = "ignore") as file:
                        file.write(str(i))
                        
                    with open("requete.py","r") as file2:
                        b = file2.read()
                        
                    liste3.append(b)

                    pos1 = str(liste3).find("span>") + 2  #on prend le premier truk span
                    pos2 = str(liste3).find("</span") - 3
                    
                    autre_def = str(i).find("Autre définition")#en gros on prend tous les titre
                    autre_def1 = str(i).find("Aucun mot trouvé")
                                #nom commun, adverbe adjectif et si y'a le parasite on l'enleve
                    if autre_def > 0:
                        pass
                    elif autre_def1 > 0:
                        pass
                    else:       #sinon on ajoute
                        a = liste3[0][pos1:pos2]                        
                        liste_mot_sens.append(a)               

                        liste3 = []     #c'est le truk qui contient nom commun
                                                                                 
                liste_mot_sens.append(str("".join(mot1) + ": FIN possibilité"+"\n"))
                
                        #en gros on prend tous les adverbe nom commun de chaque mot
                        #mes chaussures sont oranges => oki =)


        for i in liste:
            if i == []:
                pass
            else:
                try:
                    
                    path2 = "http://www.conjugaison.com/verbe/{}.html"  #recherche verbe
                    search = path2.format("".join(i))
                    
                    requete = requests.get(search)
                    page = requete.content
                    soup = BeautifulSoup(page, "html.parser")      
                    propriete = soup.find("blockquote")
                    propriete2 = soup.find("title")         #faudrai prendre le titre et comparer
                                                            #avec mot...
                    with open("requete3.html","w") as file:
                        file.write(str(propriete))
                    
                    with open("requete3.html","r") as file2:
                        b = file2.read()

                    pos1 = str(b).find("VERBE")
                    if pos1 > 0:
                        liste_mot_sens2.append("Verbe")
                    else:
                        liste_mot_sens2.append("None")
                except:
                    liste_mot_sens2.append("None, ") 
    
        #comparer avec phrase est prendre le bon truk selon modele
                    #faire avec verbe mtn et trouvé bon verbe
                    #alimente tes phrases


        print(oInput)
        print(liste_mot_sens)
        print(liste_mot_sens2)  #faut courir  une grande liste 

        phrase_simple1 = ["Forme d’article défini","Nom commun", "Verbe", "Adjectif"]

        
        try:
            if len(phrase_simple1) == len(liste_mot_sens)\
               and len(phrase_simple1) == len(liste_mot_sens2):
                print("meme longueur que la phrase simple1")

            cmpteur = 0
            cmpteur2 = 0
            occurence = list(set(liste_mot_sens) & set(phrase_simple1))

            for i in liste_mot_sens2:
                if i == "Verbe":
                    cmpteur += 1
                            
            for i in occurence:
                cmpteur2 +=1
            
            if cmpteur2 < int(len(phrase_simple1)) - 1 and  cmpteur > 0:
                
                print("c une phrase simple")

            
            print("meme schema que phrase_simple1")


        except:
            pass
         #   print("phrase non connu")
          #  phrase.append(liste_mot_sens)

            
    #il faut que ca prenne tous les titres, et que le truk disent si y'a deux nom communs
            #a la suite impo
            #reference : nom commun + adj
            #donc c l'adj
    #si on connait pas le type de phrase print("nan"), faire TOUTE LES POSSIBILITés
            #et les appends dans un fichier text

    #on ne compare plus depuis les listes mais depuis un fichier gl


    #mais quelle reference ? premier mot ?
          #je suis
          #la voiture
          #nous devons
          #les les 2 premiers mots





    
    #pronom = désigne une personne ou groupe
    #verbe = action passé, present, futur
    #compelment ajoute une information
    #article definit une chose
    #article non definit = general

    # -> il veut un cailloux marron
        #prnom verbe article nom commun adjectif
            # quelqu'un veut/vouloir/posserder un cailloux/information : marron
        



    def image_avec_image(self):

        self.phrase = ["la voiture roule sur le tram rouge"]
        self.phrase1 = ["il veut un cailloux marron"]
        self.phrase2 = ["il vole dans avec une baleine bleue"]

    #on a comparer le type de phrase,
    #on a les verbes (car ya que ca qui change dans une phrase)
    #il faudrait faire la ponctuation : respiration, emotion
    #pose toi reflechis faut que ca parle

    #il faut les propriétés physiques ... et il faut découper des video

    def analyse(self):

        self.phrase = ["la voiture roule sur le tram rouge"] #peut
        self.phrase1 = ["il veut un cailloux marron"]   #oui
        self.phrase2 = ["il vole dans avec une baleine bleue"] # non ou métaphore pour dire nager
        
language = language()
#language.liste_phrase()
#language.nettoyage()
#language.ouverture()
#language.occurence()
#language.text()
#language.fais_liste()
#language.remplissage_listee()
#language.mot_phrase()
#language.identification()
#language.les_verbes()
language.compréhension()


#faire la mis en de la liste dedans...grrr
#fsouviens toi du gros bloc, souviens toi...
