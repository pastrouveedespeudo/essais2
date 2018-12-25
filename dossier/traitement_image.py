import os
from PIL import Image
import shutil
import time
import cv2

from opération_dossier import *
from liste_traitement import *
from aimmeuble import *
from avoiture import *
from apanneau import *
from atram import *
from zzpath import *



class Traitement_image:

#1 but : faire un ficher par image
    def rognage_des_ciels(self, dossier_départ, top, height, fichier, dossier):
        """on redimensionne les éléments du dossier pour n'avoir que le
            ciel et on prend LEUR CIEL"""
        
        self.dossier_départ = dossier_départ
        self.fichier = fichier
        self.dossier = dossier
        
        self.ajout = 0
        self.dico_couleur_ct = {}
  
        os.chdir(self.dossier_départ)  #on se place dans un dossier
        liste = os.listdir(".")        
        
        for i in liste :
            print(i)
            try:
            
                self.top = top
                self.height = height

                self.lecture = Image.open(i) # on va lire tous les elements
                print("ouverture",i)                         #du dossier
           
                largeur = self.lecture.width
                hauteur = self.lecture.height
                
                self.top = self.top
                left = 0
                width = largeur
                self.hauteur = self.height
                
                rognage = (left,
                           self.top,
                           left + width,
                           self.top + self.height)

                area = self.lecture.crop(rognage)
                
                self.nom_sauvegarde = "image_rognage:" + str(i)
                area.save(self.nom_sauvegarde)
                
                ouverture = Image.open(self.nom_sauvegarde)
                
                #on prend les couleurs
                for value in ouverture.getdata(): 
                    if value in self.dico_couleur_ct.keys():
                        self.dico_couleur_ct[value] += 1     
                    else:
                        self.dico_couleur_ct[value] = 1


                couleur_image = []
                couleur_image = couleur_image[:5]
                
                for a in self.dico_couleur_ct.keys():
                    couleur_image.append(a)

                #on ajoute n + 1
                self.ajout = str(self.ajout)
                nom = "liste_couleur" + self.ajout + "= ["
                
                #self.fichier = self.fichier + self.ajout

                element = str(i)

                with open(self.fichier, "w") as file:
                    #dossier de creation dossier ex: dossier0, dossier1...
                    file.write(str(couleur_image[0]))
                    file.write(",")
                    file.write(str(couleur_image[1]))
                    file.write(",")
                    file.write(str(couleur_image[2]))
                    file.write(",")
                    file.write(str(couleur_image[3]))
                    file.write(",")
                    file.write(str(couleur_image[4]))
                    file.write(",")
       

                    file.close()
                
                    copie = i+ "" +self.fichier
                    shutil.copy(self.fichier, copie)
                    Dossier.se_placer(self, DOSSIER_TEST)
                    lisste = os.listdir(".")
                    dernier_dossier = lisste[-1]
                    Dossier.se_placer(self, self.dossier_départ)
                    shutil.move(copie,
                    r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}".format(dernier_dossier)
                                )
                    self.dico_couleur_ct = {}
            except:
                pass

#2
    def rognage_ciel(self, image, nom_sauvegarde, height, top, test):

        self.image = image
        self.nom_sauvegarde = nom_sauvegarde
        self.test = test
        
        self.top = top
        self.height = height
        
        self.lecture = Image.open(self.image)

        largeur = self.lecture.width
        hauteur = self.lecture.height
        
        self.top = self.top
        left = 0
        width = largeur
        self.hauteur = self.height
        

        rognage = (left,
                   self.top,
                   left + width,
                   self.top + self.height)


        area = self.lecture.crop(rognage)
        #area.show()
        
        area.save(self.nom_sauvegarde)

        fichier = open(self.test,"a")
        
        fichier.write("\nrognage :\n ")
        fichier.write("nom sauvegarde :" + str(self.nom_sauvegarde)+ " ,")
        fichier.write("top : " + str(self.top) + " ,")
        fichier.write("left : " + str(left) + " ,")
        fichier.write("width : " + str(width) + " ,")
        fichier.write("huateur : " + str(self.hauteur) + "\n")

                    
            



#3
    def couleur(self, image, fichier):
        """ on ecrit les couleurs présentes de NOTRE IMAGE"""
        
        self.fichier = fichier
        self.image = image
        self.dico_couleur_ct = {}
        
        ouverture = Image.open(self.image)

        for value in ouverture.getdata(): 
            if value in self.dico_couleur_ct.keys():
                self.dico_couleur_ct[value] += 1
                
            else:
                self.dico_couleur_ct[value] = 1

        couleur_image = []
        
        #on prend les 5 premieres couleurs de l'image
        for i in self.dico_couleur_ct:
            couleur_image.append(i)
        couleur_image_cinq = couleur_image[:5]
        with open(self.fichier,"a") as file:
            file.write("\n")
            file.write(str(couleur_image_cinq))
            file.close()
            

#4
    def comparage_sans_rognage(self, dossier1, image_a_compa, test, fichier):
        """on compare les images de fichier avec notre image"""
    
        self.test = test
        self.dossier1 = dossier1
        self.image_a_compa = image_a_compa
        self.fichier = fichier

        Dossier.se_placer(self, dossier1)
        liste1 = os.listdir(".")        

       # on fait défiler les dossiers du dossier
        for i in liste1:

            if i == "image_immeuble":
               i = PATH_IMMEUBLE
               
            elif i == "image_panneau":
                i = PATH_PANNEAU
                
            elif i == "image_tram" :
                i = PATH_TRAM
                
            elif i == "image_voiture":
                i = PATH_VOITURE
                
            elif i == "zzz.jpg":
                break

            Dossier.move_fichier(self, self.image_a_compa, i)
            
            #on se place dans un des dossiers
            Dossier.se_placer(self, i)
            
            liste2 = os.listdir(".")
            
            # on fait défiler les images du fichier
            for j in liste2:        

                if j == "zzz.jpg":
                    pass
                
                try:
                
                    matches_biatches = 600

                    im1 = cv2.imread(self.image_a_compa, 0)
                    im2 = cv2.imread(j, 0)

                    orb = cv2.ORB_create()

                    kp1, des1 = orb.detectAndCompute(im2, None)
                    kp2, des2 = orb.detectAndCompute(im1, None)

                    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

                    matches = bf.match(des1,des2)
                    matches = sorted(matches, key = lambda x:x.distance)

                    im3 = cv2.drawMatches(im1,kp1,im2,kp2,
                                          matches[:matches_biatches],
                                          None, flags=2)

                    self.compteur = 0
                    
                    for match in matches[:matches_biatches]:
                        self.compteur += 1
                    print(j, "nombre occurence : " ,self.compteur)

                    self.dossier1 = str(self.dossier1)
                    self.copie = str("2" + j)

                    if self.compteur > 200:
                        
                        shutil.copy(j, self.copie)
                        shutil.move(self.copie, self.test)
                        
                        Traitement_image.match(self, self.compteur, self.fichier,
                                                self.dossier1 )
                        # on enregisre les données dans fichier test
                        
                except:
                    pass
      
        Dossier.move_fichier(self, self.image_a_compa, PATH_IMAGE)

           
#5
    def match(self, compteur, fichier, dossier): 

        self.compteur = compteur
        self.fichier = fichier
        self.dossier = self.dossier

        file = open (self.fichier, "a")
        file.write(self.dossier)
        file.write(self.compteur)
        file.write(",\n")
        file.close()

#6
    def comparage_rognage_des_images(self, dossier1, image_a_compa, test):
        """on compare notre image avec les images du fichier reziser"""
    
        print("session comaparage avec rognage")
        
        self.dossier1 = dossier1
        self.test = test
        self.image_a_compa = image_a_compa

        Dossier.se_placer(self, dossier1)
        liste1 = os.listdir(".")
        
        for i in liste1:

            if i == "image_immeuble":
               i = PATH_IMMEUBLE
               
            elif i == "image_panneau":
                i = PATH_PANNEAU
                
            elif i == "image_tram" :
                i = PATH_TRAM
                
            elif i == "image_voiture":
                i = PATH_VOITURE
                
            elif i == "zzz.jpg":
                break
            try :
                Dossier.move_fichier(self, self.image_a_compa, i)
            except:
                pass
            
            
            Dossier.se_placer(self, i)
            liste2 = os.listdir(".")
            
            for j in liste2:
                if j == "zzz.jpg":
                    pass
 
                try :
                    
                    self.leture_image1 = Image.open(self.image_a_compa)
                    self.lecture_i = Image.open(j)
                    
                    largueur = self.leture_image1.width 
                    hauteur = self.leture_image1.height

                    largueur_i = self.lecture_i.width 
                    hauteur_i = self.lecture_i.height

                    nouvelle_taille = self.lecture_i.resize(
                        (largueur_i, hauteur),
                        Image.ANTIALIAS)
                    
                    nouvelle_taille.save(j) # on resize l'image, on save

                    matches_biatches = 600

                    im1 = cv2.imread(self.image_a_compa, 0)
                    im2 = cv2.imread(j, 0)

                    orb = cv2.ORB_create()

                    kp1, des1 = orb.detectAndCompute(im2, None)
                    kp2, des2 = orb.detectAndCompute(im1, None)

                    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

                    matches = bf.match(des1,des2)

                    matches = sorted(matches, key = lambda x:x.distance)


                    im3 = cv2.drawMatches(im1,kp1,im2,kp2,
                                          matches[:matches_biatches],
                                          None, flags=2)
                    
                    nouvelle_taille = self.lecture_i.resize(
                        (largueur_i, hauteur_i), Image.ANTIALIAS )
                    
                    nouvelle_taille.save(j) # on remet l'image a sa taille origine

                    self.compteur = 0
                    for match in matches[:matches_biatches]:
                        self.compteur += 1
                    print(j, "occurence : ", self.compteur)

                    self.dossier1 = str(self.dossier1)
                    
                    self.copie = str("2" +j)

                    if self.compteur > 200:

                        shutil.copyfile(j, self.copie)
                        shutil.move(self.copie, self.test)
                        
                        Traitement_image.match_sans_rognage(self,
                                            self.compteur, self.fichier,
                                                self.dossier1)
                        
                except:
                    pass
                
#6
    def match_sans_rognage(self, compteur, fichier, dossier): 

        self.compteur = compteur
        self.fichier = fichier
        self.dossier = self.dossier

        file = open (self.fichier, "a")
        file.write("occurence avec resize : ")
        file.write("\n")
        file.write(self.dossier)
        file.write(self.compteur)
        file.write("\n")
        file.close()        



    def ouverture_fichier(self, fichier, test):

        self.fichier = fichier
        self.test = test
        
        self.image = Image.open(self.fichier)
        fichier_test = self.test
        
        file = open(fichier_test,"a") 
        file.write("image: ")
        file.write(str(self.fichier))
        file.close()


    def copie(self, image, copie):

        self.image = image
        self.copie = copie

        image_a_copier = Image.open(self.image)
        image_a_copier = shutil.copyfile(self.image, self.copie)


            

    def couleurs_ciels(self):

        self.fichier = fichier
        self.image = image
        self.dico_couleur_ct = {}
        
        ouverture = Image.open(self.image)

        for value in ouverture.getdata(): 
            if value in self.dico_couleur_ct.keys():
                self.dico_couleur_ct[value] += 1
                
            else:
                self.dico_couleur_ct[value] = 1

        with open(self.fichier,"a") as file:
            file.write("\n")
            file.write(str(self.dico_couleur_ct))
            file.close()
                
        
        
    
    def nom_dossier(self):


        liste_dossier = os.listdir(".")
        
        b = len(liste_dossier) - 2
        c = liste_dossier[b]
        
        liste_doss = []
        #faire en sorte que ca prenne 
        with open(c) as file :
            for i in file:
                liste_doss.append(i)

    def nom_dossier2(self):


        liste_dossier = os.listdir(".")
        
        b = len(liste_dossier) - 3
        c = liste_dossier[b]
        
        liste_doss = []
        #faire en sorte que ca prenne 
        with open(c) as file :
            for i in file:
                liste_doss.append(i)



#pour pouvoir importer et recup la liste

    def couleur_image(self, image, doss, doss1, doss2):

        self.image = image
        self.doss1 = doss1
        self.doss2 = doss2
        self.doss = doss
        
        self.couleur_image = []
        self.dico_couleur_ct = {}
        dico = {}

        os.chdir(doss)

        im = Image.open(self.image)

        
        for value in im.getdata(): 
            if value in self.dico_couleur_ct.keys():
                self.dico_couleur_ct[value] += 1
            else:
                self.dico_couleur_ct[value] = 1
                
     
        for a in self.dico_couleur_ct.keys():
            self.couleur_image.append(a)
        self.couleur_image = self.couleur_image[:5]

        for i in self.dico_couleur_ct.keys():
            self.couleur_image.append(i)

        self.couleur_cinq = self.couleur_image[:5]
        with open("image_prio.py","w") as file:
            
            file.write(str(self.couleur_cinq[0]))
            file.write(",")
            file.write(str(self.couleur_cinq[1]))
            file.write(",")
            file.write(str(self.couleur_cinq[2]))
            file.write(",")
            file.write(str(self.couleur_cinq[3]))
            file.write(",")
            file.write(str(self.couleur_cinq[4]))


        try:
            Dossier.se_placer(self, self.doss1)
            lisste = os.listdir(".")
            dernier_dossier = lisste[-1]
            Dossier.se_placer(self, self.doss2)
            shutil.move("image_prio.py",
            r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}".format(dernier_dossier))

        except:
            pass

        
    def compa(self, image, dossier):
        
        self.image = image
        self.dossier = dossier

        self.couleur_image = []
        self.dico_couleur_ct = {}
        dico = {}
        
        im = Image.open(self.image)
        
        for value in im.getdata(): 
            if value in self.dico_couleur_ct.keys():
                self.dico_couleur_ct[value] += 1
            else:
                self.dico_couleur_ct[value] = 1
                
        for a in self.dico_couleur_ct.keys():
            self.couleur_image.append(a)
        self.couleur_image = self.couleur_image[:5]

        for i in self.dico_couleur_ct.keys():
            self.couleur_image.append(i)

        self.couleur_cinq = self.couleur_image[:5]

        
        os.chdir(self.dossier)
        liste = os.listdir(".")
        dosss = liste[-1]        

        self.dossier = r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}".format(dosss)
        os.chdir(self.dossier)
        listee = os.listdir(".")
        for i in listee:
            print(i)
            file = open(i,"a")
            file.write("\n")

            file.write(str(self.couleur_cinq[0]))
            file.write(",")
            file.write(str(self.couleur_cinq[1]))
            file.write(",")
            file.write(str(self.couleur_cinq[2]))
            file.write(",")
            file.write(str(self.couleur_cinq[3]))
            file.write(",")
            file.write(str(self.couleur_cinq[4]))
            file.close()
        
            
    def comparaison_des_couleurs(self, dossier):

        self.dossier = dossier

        os.chdir(self.dossier)
        liste = os.listdir(".")
        dosss = liste[-1]        

        self.dossier = r"C:\Users\jeanbaptiste\ste fois c la bonne\dossier test 1\{}".format(dosss)
        os.chdir(self.dossier)
        liste = os.listdir(".")
        
        liste1 = []
        liste2 = []

        for i in liste:
            if i != "image_prio":
                file = open(i, "r")
                liste1.append(file.read())
                
                with open("image_prio.py","r") as file2:
                    liste2.append(file2.read())


            o = list(set(liste1) & set(liste2))
            if o == []:
                print("no occurence")
            else:
                print("occurence")
            
                with open("occurence_couleur.py","a") as file:
                    file.write(str(liste1))
                    file.write("\n")
                    file.write(str(liste2))
                    file.write("\n")
                    file.write(str(0))
                    file.write("\n")
                    file.write(i)
                    file.write("\n")
                
            liste1 = []
            liste1 = []
           
                

            

        





#se placer faire le truk dernier doss
#move zzz dedans
                    
