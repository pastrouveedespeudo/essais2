# -*- coding: utf-8 -*-

from path import *
from internet import *
from fichier import *
from phrase import *
import itertools
import time
from itertools import combinations


class Langage:


    def question(self):

        self.oInput = input("rentre une phrase")

        
    def cherche_dico(self):

        self.liste_input = [[],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[]]
        
        self.liste_mot_dico = []
        
        self.structure_phrase = []
        self.structure_phrase2 = []

        self.liste_verbe = []

        self.compteur1 = 0
        
        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)



        c = 1
        self.compteur1 = self.compteur1 + 1

        listee.listess(self)

        for phrase in self.phrase:
                
            if len(phrase)-1 == self.compteur1:
                print("\n","schema", phrase[0],"\n")
                un = True

            else:
                print("no match")
                un = False


            if un == True:
                
                for i in self.liste_input:
                    if i == []:
                        break
                    else:
                        mot = str("".join(i))
                        print(mot)
                        internet.search(self, mot, self.liste_mot_dico)  
                
                        internet.search_verbe(self, DICO_VERBE, mot,
                                    self.liste_verbe, REQUETE, "w", "r")

                        if phrase[c] == "Verbe":
                            self.liste_mot_dico = self.liste_verbe
                        for i in self.liste_mot_dico:
                            if phrase[c] == i:
                                print("matches : ", i)
                            break

                        self.liste_mot_dico = []
                        self.liste_verbe = []
                        c+=1
                
                print("c'est une phrase", phrase[0],
                        "mais y'a une erruer")
                break

            elif un == False:
                Langage.nouvelle_phrase()
                break

            
    def nouvelle_phrase(self):

        self.liste_input = [[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[],[]]

        self.liste_stockage = [[],[],[],[],[],[],[],[],[],
                               [],[],[],[],[],[],[],[],[],
                               [],[],[],[],[],[],[],[],[]]
        self.compteur1 = 0
        
        self.liste_mot_dico = []
        self.liste_verbe = []

        self.liste_melange = []
        self.liste_melange_demi_temps = []

        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)
                
        for i in self.liste_input:         
            mot = str("".join(i))
            print(mot)
            
            if mot == " " or mot == "":
                break
        
            internet.search(self, mot, self.liste_mot_dico)

            internet.search_verbe(self, DICO_VERBE, mot,
                                        self.liste_verbe, REQUETE, "w", "r")
    
            if self.liste_verbe[0] == "None":
                pass
            elif self.liste_verbe[0] == "Verbe":
                self.liste_mot_dico.append("Verbe")

            c3 = 0
            for i in self.liste_mot_dico:
                self.liste_stockage[c3].append(self.liste_mot_dico)
                self.liste_mot_dico = []
                self.liste_verbe = []
                c3 += 1

        liste = []
        c4 = 0
        try :
            for i in self.liste_stockage:
                liste.append(self.liste_stockage[0][c4][-1])
                c4 += 1
        except:
            pass
        finally:
            
            if self.oInput[-1] == "?":
                nom_phrase = "phrase interogrative"
                
            
            elif self.oInput[-1] == "!":
                nom_phrase = "phrase exclamative"
                

            else:
                nom_phrase = "phrase " + str(liste[0])
                
            liste.insert(0, nom_phrase)            
            print(liste)
            Langage.ecriture_phrase(liste)


            
    def ecriture_phrase(self, liste3):

        liste = []
        liste2 = []
    
        self.liste3 = liste3

        with open("phrase.py","r", encoding = "utf-8") as file:
            a = file.read()

        liste.append(a)

        liste2 = liste[0][:-2]
                
        with open("phrase.py", "w", encoding = "utf-8") as file:
            file.write(str(liste2))

        with open("phrase.py", "a", encoding = "utf-8") as file:
            file.write(",")
            file.write("\n")
            file.write("            ")
            file.write(str(self.liste3))
            file.write("] ")


    def reconnaissance_type_phrase_spé(self):

        self.liste_input = [[],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[]]

        self.compteur1 = 0
        
        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)
        for i in self.liste_input:
                
                if i == []:
                    break
                
                else:
                    mot = str("".join(i))
                    print(mot)
    


    def reconnaissance_phrase(self):
        pass

    #la vache vole [impo]
    #je vole avecu ne baleine blue[métaphore nager]
    #le singe mange des bananes[possible]


    def proba(self):
        pass
    #% que ce soit ste phrase

    def arbre_proba(self):
        pass

    #voiture -> discussion de sport
    #rouge -> discussion d'ésthetique
    #sport + esté ?

    def repondre(self):
        pass
    #ca repond.
    #sans phrase prédéfini qu'en scrappant...

    def imagerie_mentale(self):
        pass
    #on lui dit un truk ca fait image image
    #et ca les mélanges


if __name__ == "__main__":

    Langage = Langage()
    Langage.question()
    Langage.cherche_dico()

