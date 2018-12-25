from PIL import Image


class image:

    def image_notion_passée(self):
        pass
    #gris

    def image_resize(self, image):
        self.image = image
        

    #depend des propriete physique + de la phrase
    def image(self, droite, gauche, haut, bas,
              image1, image2, image3):

        self.droite = droite
        self.gauche = gauche
        self.haut = haut
        self.bas = bas
        
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3

        picture1 = Image.open(self.image1)
        height1 = picture1.height 
        width1 = picture1.width

        picture2 = Image.open(self.image2)
        height2 = picture2.height 
        width2 = picture2.width

        picture3 = Image.open(self.image3)
        height3 = picture3.height 
        width3 = picture3.width 

        result_width = width1 + width2
        result_height = max(height1, height2)

        result = Image.new('RGB', (result_width, result_height))
        result.paste(im = picture1, box = (0, 100))#droite/bas/- = gauche/-haut
        result.paste(im = picture2, box =(width1, 0))#droite/bas/- = gauche/-haut
        result.paste(im = picture3, box =(100, 0))
        result.show()

        
        #result = Image.new('RGB', (result_width+600, result_height+600))
        #result.paste(im = picture1, box = (0, 200))#droite/bas/- = gauche/-haut
        #result.paste(im = picture2, box =(0, -600))#droite/bas/- = gauche/-haut
        #result.paste(im = picture3, box =(0, 0))
        # -> haut bas

        #y'a un truk a faire avec traitement mot ici dans les para
        #enregistrer l'image

    def couleur_image(self,image):
        self.image = image

        picture = Image.open(self.image).convert("LA")
        
        picture.show()
        picture.save("passé_"+self.image+".png")



        #suite logique du truk d'en haut on prend l'image
        #on prendre le temps du verbe
        #on met tout en noir et blanc si passé/imparfait















        
image = image()
#image.image("","","","",
#            "chat_gris.jpg",
#            "chat_roux.jpg","chat_roux.jpg")
image.couleur_image("chat_roux.jpg")
