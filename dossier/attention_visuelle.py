import cv2
import matplotlib
from pylab import *
from PIL import *
import os
import shutil

class Découpage:
    
#7.2, 12.8
    
    def découpe(self, image, div_hauteur, div_largeur, dossier):

        self.image = image
        self.dossier = dossier
        
        im = Image.open(self.image)
        
        im_hauteur = im.height
        im_largeur = im.width

        self.div_hauteur = div_hauteur
        self.div_largeur = div_largeur
        
        a = 0
        i = 0
        
        left = 0
        top = 0
        self.div_hauteur = div_hauteur #7.2 nombre fois (petite)
        self.div_largeur = div_largeur #12.8
        
        height = im_hauteur / self.div_hauteur
        width = im_largeur / self.div_largeur
        #print(im_hauteur)

  
        while left < im_largeur: 
                
            rectangle = [left, top, left+width, top+height]
            #print(rectangle)
            
            area = im.crop(rectangle)
            b = "{}.jpg".format(a)
            area.save(b)

            
            shutil.move(b, self.dossier)
            a += 1
            
            left += width
            
            if left >= im_largeur:
                
                left = 0
                top += height

                if top >= im_largeur:
                    print("fini")
                    break


            
            












            
