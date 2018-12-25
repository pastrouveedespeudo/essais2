from internet import *
from path import *
from doc_question import *


class Dico:

    def question(self):
        
        print("le crayon est vert et sur la table rouge")
        self.oInput = input("rentre une phrase simple")
        
        liste_self_oInput = []
        liste_self_oInput.append(str(self.oInput))
        fichier.ecriture_phrase(self, liste_self_oInput)


    def dictionnaire(self):

        self.liste_input = [[],[],[],[],[],[],[],[],[],[],[],[],
                            [],[],[],[],[],[],[],[]]

        self.liste_mot_dico = []
        self.liste_verbe = []

        liste_ecriture = []

        self.liste_traitement = [[],[],[],[],[],[],[],[],[],[],[],[],
                                [],[],[],[],[],[],[],[]]

        self.compteur1 = 0
        c = 0
        
        for i in self.oInput:
            if i == " ":
                self.compteur1 += 1
            else:
                self.liste_input[self.compteur1].append(i)

        for i in self.liste_input:
            if i == []:
                pass
            else:
                i = "".join(i)
                print(i)
                
                internet.search(self, i, self.liste_mot_dico)
                
                internet.search_verbe(self, DICO_VERBE, i,
                                        self.liste_verbe, "requete.py", "w", "r")
    
                #truk traitement
                print(self.liste_mot_dico)
                print(self.liste_verbe)

                liste_i = []
                liste_i.append(i)
                
                self.liste_traitement[c].append(i)
                self.liste_traitement[c].append(self.liste_mot_dico[0])
                self.liste_traitement[c].append(self.liste_verbe[0])
                c += 1
                
                liste_i = []
                self.liste_mot_dico = []
                self.liste_verbe = []

        print(self.liste_traitement)

    def prenom(self):
        pass
        #appeler la fonction
        #internet

    
    def prenom_premier(self):
        pass
        #si c un nom commun contre un prenom en début alors prenom gagne

        #faire les deux oncditions



    def condition_article(self):
        #faire les para
        
        c1 = 0
        c2 = 0
        for i in liste:
            if i == []:
                pass
            else:
                for i in range(len(liste[c1])):
                    art = str(liste[c1]).find(str("Article"))
                    art1 = str(liste[c1]).find(str("article"))
                    if art > 0 or art1 > 0 and liste[c1 + 1][2] == "Verbe":
                        del liste[c1 + 1][2]
                    print(liste[c1][0], liste[c1][1])
                    c2+=1
                    break

            c1 += 1
            c2 = 0

        print(liste)



    def nom_commun(self):
        
        c1 = 0

        for i in liste:
            if i == []:
                pass
            else:
                for i in range(len(liste[c1])):
                    art = str(liste[c1]).find(str("Article"))
                    art1 = str(liste[c1]).find(str("article"))
                    print(liste[c1][1])
                    if liste[c1][1] == "Nom commun":
                
                        print("oui")#recherche image
                    break
            c1 += 1

            #faire les parametres
            #inclure la recherche image
                    

    def position(self):
        self.liste_direction = ["droite","gauche","haut","bas","sur"]

    def temps(self):

        self.temps = ["hier","passé","demain","après demain","aujourd'hui"]
        #prendre le temps des truk la fin des verbes and mot clé
        #avant, apres, hier
        #relier avec image/internet

    def exclusion(self):
        pass
        #le chien ou le chat apel 2 images

    def inclusion(self):
        pass
        #le chien et le chat apel 1 image

    def taille(self):
        pass
        #le petit chien parle avec le gros chat




        
    #on trouve les mots clés et on dis quoi faire
    #ex : trouve adjectif dis moi mot

    #ici on dit a l'image comment etre
        #a droite alors 100
        #a gauche alors -100
        #sur la table alors table milieu et on met le crayon en haut


           
